from __future__ import annotations

import json
import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

import pandas as pd


DATA_DIR = Path(__file__).parent / "data" / "raw"
OUTPUT_DIR = Path(__file__).parent / "data"
CHANNEL_RANKING_PREFIX = "CHANNEL_RANKING_"
CHANNEL_RANKING_OUTPUT = OUTPUT_DIR / "channel_ranking_long.csv"
EFFECT_CURVE_OUTPUT = OUTPUT_DIR / "effect_curve_long.csv"
MEDIARADAR_OUTPUT = OUTPUT_DIR / "mediaradar_chomps_long.csv"
COMMSPOINT_MIX_OUTPUT = OUTPUT_DIR / "commspoint_mix_long.csv"
COMMSPOINT_MULTICHANNEL_CURVE_OUTPUT = OUTPUT_DIR / "commspoint_multichannel_curve_long.csv"
MEDIA_CONSUMPTION_FILES = [
    "MEDIA_CONSUMPTION_DAY.csv",
    "MEDIA_CONSUMPTION_WEEK.csv",
    "MEDIA_CONSUMPTION_WEEKEND.csv",
]
MEDIA_CONSUMPTION_OUTPUT_SUFFIX = "_standardized"

MONTH_MAP = {
    "JAN": 1,
    "FEB": 2,
    "MAR": 3,
    "APR": 4,
    "MAY": 5,
    "JUN": 6,
    "JUNE": 6,
    "JUL": 7,
    "JULY": 7,
    "AUG": 8,
    "SEP": 9,
    "SEPT": 9,
    "OCT": 10,
    "NOV": 11,
    "DEC": 12,
}


def _snowflake_safe_columns(columns: List[str]) -> List[str]:
    safe_columns: List[str] = []
    seen: Dict[str, int] = {}

    for idx, column in enumerate(columns):
        cleaned = re.sub(r"[^0-9a-z]+", "_", column.strip().lower())
        cleaned = cleaned.strip("_")

        if not cleaned:
            cleaned = f"column_{idx + 1}"

        base_name = cleaned
        suffix = 1
        while cleaned in seen:
            suffix += 1
            cleaned = f"{base_name}_{suffix}"
        seen[cleaned] = 1
        safe_columns.append(cleaned)

    return safe_columns


def _standardized_copy_path(csv_path: Path, output_dir: Path) -> Path:
    return output_dir / f"{csv_path.stem}{MEDIA_CONSUMPTION_OUTPUT_SUFFIX}{csv_path.suffix}"


def standardize_media_consumption_headers(
    source_dir: Path, file_names: List[str], output_dir: Path
) -> List[Path]:
    updated_paths: List[Path] = []

    for file_name in file_names:
        csv_path = source_dir / file_name
        if not csv_path.exists():
            print(f"[WARN] Media consumption file not found: {csv_path}")
            continue

        output_path = _standardized_copy_path(csv_path, output_dir)
        df = pd.read_csv(csv_path)
        original_columns = df.columns.tolist()
        safe_columns = _snowflake_safe_columns(original_columns)
        df.columns = safe_columns
        df.to_csv(output_path, index=False)
        updated_paths.append(output_path)

        if safe_columns == original_columns:
            print(f"Copied {file_name} to {output_path.name} (already Snowflake-friendly)")
        else:
            print(f"Standardized headers for {file_name} -> {output_path.name}")

    return updated_paths


@dataclass
class FileSummary:
    file_name: str
    row_count: Optional[int]
    column_count: int
    sample_columns: List[str]

    def to_dict(self) -> Dict[str, object]:
        return {
            "file": self.file_name,
            "rows": self.row_count,
            "columns": self.column_count,
            "sample_columns": self.sample_columns,
        }


def summarize_csvs(data_dir: Path, sample_rows: int = 3) -> List[FileSummary]:
    summaries: List[FileSummary] = []

    for csv_path in sorted(data_dir.glob("*.csv")):
        read_kwargs = {"nrows": 0}
        preview_kwargs = {"nrows": sample_rows}
        if csv_path.name == "MEDIARADAR_CHOMPS.csv":
            read_kwargs["engine"] = "python"
            preview_kwargs["engine"] = "python"

        try:
            header_frame = pd.read_csv(csv_path, **read_kwargs)
            column_count = len(header_frame.columns)
            sample_columns = header_frame.columns.tolist()[: min(column_count, 5)]
        except Exception as err:  # pragma: no cover - defensive logging
            print(f"[WARN] Failed to read header from {csv_path.name}: {err}")
            continue

        row_count = _count_rows(csv_path)

        summaries.append(
            FileSummary(
                file_name=csv_path.name,
                row_count=row_count,
                column_count=column_count,
                sample_columns=sample_columns,
            )
        )

        try:
            preview = pd.read_csv(csv_path, **preview_kwargs)
            print(f"\nPreview of {csv_path.name} (first {sample_rows} rows):")
            print(preview.head(sample_rows))
        except Exception as err:  # pragma: no cover - best-effort preview
            print(f"[WARN] Unable to load preview for {csv_path.name}: {err}")

    print("\nCSV file summaries:")
    print(json.dumps([summary.to_dict() for summary in summaries], indent=2))

    return summaries


def _count_rows(csv_path: Path) -> Optional[int]:
    try:
        with csv_path.open("r", encoding="utf-8", errors="ignore") as handle:
            return max(sum(1 for _ in handle) - 1, 0)
    except OSError:
        return None


def extract_strategy(file_name: str) -> str:
    base = file_name.replace(".csv", "")
    strategy_part = base.replace(CHANNEL_RANKING_PREFIX, "")
    # if "_BFY" in strategy_part:
    #     strategy_part = strategy_part.split("_BFY", 1)[0]
    return strategy_part.lower()


def combine_channel_rankings(data_dir: Path, output_path: Path) -> Path:
    ranking_files = sorted(data_dir.glob(f"{CHANNEL_RANKING_PREFIX}*.csv"))
    if not ranking_files:
        raise FileNotFoundError("No CHANNEL_RANKING files were found.")

    frames: List[pd.DataFrame] = []
    expected_columns: Optional[List[str]] = None

    for csv_path in ranking_files:
        df = pd.read_csv(csv_path)
        if expected_columns is None:
            expected_columns = df.columns.tolist()
        elif df.columns.tolist() != expected_columns:
            raise ValueError(
                f"CHANNEL_RANKING column mismatch in {csv_path.name}. "
                "Ensure all strategy files share the same schema."
            )
        
        # remove any rows where channel is null
        df = df.dropna(subset=["CHANNEL"])

        df.insert(0, "strategy", extract_strategy(csv_path.name))
        frames.append(df)

    combined = pd.concat(frames, ignore_index=True)

    # make sure all column names are lowercase
    combined.columns = combined.columns.str.lower()

    combined.to_csv(output_path, index=False)
    print(f"Saved combined channel ranking table to {output_path}")
    return output_path


def melt_effect_curve(data_dir: Path, output_path: Path) -> Path:
    effect_path = data_dir / "EFFECT_CURVE.csv"
    if not effect_path.exists():
        raise FileNotFoundError(effect_path)

    df = pd.read_csv(effect_path)
    if "BUDGET" not in df.columns:
        raise ValueError("EFFECT_CURVE.csv must contain a BUDGET column.")

    long_df = (
        df.melt(id_vars=["BUDGET"], var_name="objective_channel", value_name="effect_score")
        .dropna(subset=["effect_score"])
        .reset_index(drop=True)
    )

    objectives_channels = long_df["objective_channel"].str.split(" - ", n=1, expand=True)
    long_df["objective"] = objectives_channels[0].str.strip().str.lower()
    long_df["channel"] = objectives_channels[1].str.strip().str.lower()
    long_df = long_df.drop(columns=["objective_channel"])
    long_df = long_df.rename(columns={"BUDGET": "budget"})
    long_df = long_df[["budget", "objective", "channel", "effect_score"]]

    long_df.to_csv(output_path, index=False)
    print(f"Saved melted effect curve table to {output_path}")
    return output_path


def reshape_mediaradar(data_dir: Path, output_path: Path) -> Path:
    mediradar_path = data_dir / "MEDIARADAR_CHOMPS.csv"
    if not mediradar_path.exists():
        raise FileNotFoundError(mediradar_path)

    df = pd.read_csv(mediradar_path, thousands=",", engine="python")
    id_columns = [
        "ADVERTISER",
        "BRAND",
        "MEDIA_GROUP",
        "MEDIA",
        "MEDIA_OWNER",
        "DOW",
        "NATIONAL/LOCAL",
        "MARKET",
        "PROGRAM",
        "PROGRAM_GENRE",
        "DAYPART",
        "PROPERTY",
    ]

    missing_cols = [col for col in id_columns if col not in df.columns]
    if missing_cols:
        raise ValueError(f"MEDIARADAR_CHOMPS is missing identifier columns: {missing_cols}")

    metric_pattern = re.compile(r"^(?P<period>[A-Z]+_\d{4})__(?P<metric>\$|UNITS)$")
    period_to_cols: Dict[str, Dict[str, str]] = {}

    for column in df.columns:
        match = metric_pattern.match(column)
        if not match:
            continue
        period_to_cols.setdefault(match.group("period"), {})[match.group("metric")] = column

    if not period_to_cols:
        raise ValueError("No month/year metric columns detected in MEDIARADAR_CHOMPS.")

    records: List[Dict[str, object]] = []
    for _, row in df.iterrows():
        base_attributes = row[id_columns].to_dict()
        for period_token, metric_cols in period_to_cols.items():
            spend = row.get(metric_cols.get("$"))
            units = row.get(metric_cols.get("UNITS"))
            if pd.isna(spend) and pd.isna(units):
                continue

            flight_date = _parse_period(period_token)
            record = dict(base_attributes)
            record["flight_date"] = flight_date
            record["spend_usd"] = spend
            record["units"] = units
            records.append(record)

    long_df = pd.DataFrame.from_records(records)
    long_df["flight_date"] = pd.to_datetime(long_df["flight_date"])
    sort_cols = ["ADVERTISER", "BRAND", "flight_date"]
    sort_cols = [col for col in sort_cols if col in long_df.columns]
    long_df = long_df.sort_values(sort_cols).reset_index(drop=True)

    long_df.columns = (
        long_df.columns.str.lower()
        .str.replace(r"[^0-9a-z]+", "_", regex=True)
        .str.strip("_")
    )

    if "market" in long_df.columns:
        def _normalize_market(value: object) -> object:
            if pd.isna(value):
                return value
            cleaned = str(value).strip()
            if not cleaned:
                return cleaned
            cleaned = re.sub(r"^\*+\s*", "", cleaned)
            cleaned = re.sub(r"[^\w]+", "_", cleaned)
            cleaned = cleaned.strip("_")
            return cleaned.upper()

        long_df["market"] = long_df["market"].apply(_normalize_market)

    long_df.to_csv(output_path, index=False)
    print(f"Saved MEDIARADAR long table to {output_path}")
    return output_path


def _parse_period(period_token: str) -> datetime:
    try:
        month_str, year_str = period_token.split("_", 1)
        month = MONTH_MAP[month_str.upper()]
        return datetime(int(year_str), month, 1)
    except (ValueError, KeyError) as err:
        raise ValueError(f"Unrecognized period token '{period_token}' in MEDIARADAR data.") from err


def extract_mix_type(file_name: str) -> str:
    """Extract mix type from COMMSPOINT MIX file name."""
    base = file_name.replace(".csv", "").replace("COMMSPOINT_", "")
    # Handle special case for 2025_BASELINE_MIX
    if base.startswith("2025_"):
        return "2025_baseline"
    return base.lower().replace("_mix", "")


def combine_commspoint_mix(data_dir: Path, output_path: Path) -> Path:
    """Combine COMMSPOINT MIX files (BASELINE, BALANCED_REACH, BRAND_IMPACT, CONVERSION_FOCUSED)."""
    mix_files = sorted(data_dir.glob("COMMSPOINT_*_MIX.csv"))
    if not mix_files:
        print("[WARN] No COMMSPOINT MIX files found.")
        return output_path

    frames: List[pd.DataFrame] = []
    expected_columns: Optional[List[str]] = None

    for csv_path in mix_files:
        df = pd.read_csv(csv_path)
        if expected_columns is None:
            expected_columns = df.columns.tolist()
        elif df.columns.tolist() != expected_columns:
            raise ValueError(
                f"COMMSPOINT MIX column mismatch in {csv_path.name}. "
                "Ensure all mix files share the same schema."
            )
        
        # Remove any rows where channel is null or empty
        df = df.dropna(subset=["CHANNEL"])
        df = df[df["CHANNEL"].str.strip() != ""]
        
        # Add mix_type column
        mix_type = extract_mix_type(csv_path.name)
        df.insert(0, "mix_type", mix_type)
        frames.append(df)

    if not frames:
        print("[WARN] No valid data found in COMMSPOINT MIX files.")
        return output_path

    combined = pd.concat(frames, ignore_index=True)
    
    # Make sure all column names are lowercase
    combined.columns = combined.columns.str.lower()
    
    combined.to_csv(output_path, index=False)
    print(f"Saved combined COMMSPOINT MIX table to {output_path}")
    return output_path


def combine_commspoint_multichannel_curves(data_dir: Path, output_path: Path) -> Path:
    """Combine and melt COMMSPOINT MULTICHANNEL_CURVE files (1PLUS, 3PLUS)."""
    curve_files = sorted(data_dir.glob("COMMSPOINT_MULTICHANNEL_CURVE_*.csv"))
    if not curve_files:
        print("[WARN] No COMMSPOINT MULTICHANNEL_CURVE files found.")
        return output_path

    frames: List[pd.DataFrame] = []
    
    for csv_path in curve_files:
        df = pd.read_csv(csv_path)
        
        # Extract reach threshold from filename (1PLUS or 3PLUS)
        if "1PLUS" in csv_path.name:
            reach_threshold = "1plus"
        elif "3PLUS" in csv_path.name:
            reach_threshold = "3plus"
        else:
            reach_threshold = "unknown"
        
        # Ensure BUDGET column exists
        if "BUDGET" not in df.columns:
            raise ValueError(f"COMMSPOINT MULTICHANNEL_CURVE file {csv_path.name} must contain a BUDGET column.")
        
        # Melt the dataframe: BUDGET and CHANNEL_MIX stay as id_vars, all channel columns become rows
        id_vars = ["BUDGET", "CHANNEL_MIX"]
        value_vars = [col for col in df.columns if col not in id_vars]
        
        long_df = df.melt(
            id_vars=id_vars,
            value_vars=value_vars,
            var_name="channel",
            value_name="effect_score"
        )
        
        # Remove rows where effect_score is null
        long_df = long_df.dropna(subset=["effect_score"])
        
        # Add reach_threshold column
        long_df.insert(0, "reach_threshold", reach_threshold)
        
        # Rename columns to lowercase
        long_df = long_df.rename(columns={
            "BUDGET": "budget",
            "CHANNEL_MIX": "channel_mix"
        })
        
        # Reorder columns
        long_df = long_df[["reach_threshold", "budget", "channel", "channel_mix", "effect_score"]]
        
        # Normalize channel names to lowercase
        long_df["channel"] = long_df["channel"].str.lower()
        
        frames.append(long_df)

    if not frames:
        print("[WARN] No valid data found in COMMSPOINT MULTICHANNEL_CURVE files.")
        return output_path

    combined = pd.concat(frames, ignore_index=True)
    
    combined.to_csv(output_path, index=False)
    print(f"Saved combined COMMSPOINT MULTICHANNEL_CURVE table to {output_path}")
    return output_path


def run_pipeline() -> None:
    print("Starting CSV review...")
    summarize_csvs(DATA_DIR)

    print("\nStandardizing media consumption headers...")
    standardize_media_consumption_headers(DATA_DIR, MEDIA_CONSUMPTION_FILES, OUTPUT_DIR)

    print("\nCombining channel ranking files...")
    combine_channel_rankings(DATA_DIR, CHANNEL_RANKING_OUTPUT)

    print("\nMelting effect curve data...")
    melt_effect_curve(DATA_DIR, EFFECT_CURVE_OUTPUT)

    print("\nReshaping MEDIARADAR CHOMPS data...")
    reshape_mediaradar(DATA_DIR, MEDIARADAR_OUTPUT)

    print("\nCombining COMMSPOINT MIX files...")
    combine_commspoint_mix(DATA_DIR, COMMSPOINT_MIX_OUTPUT)

    print("\nCombining COMMSPOINT MULTICHANNEL_CURVE files...")
    combine_commspoint_multichannel_curves(DATA_DIR, COMMSPOINT_MULTICHANNEL_CURVE_OUTPUT)

    print("\nPipeline complete.")


if __name__ == "__main__":
    run_pipeline()

