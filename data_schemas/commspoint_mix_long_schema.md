# Table Name: COMMSPOINT_MIX_LONG

## Table Description
Per-strategy media mix allocation table showing budget allocation, gross rating points (GRPs), and impressions by channel and channel group across different marketing mix strategies (baseline, balanced reach, brand impact, conversion focused). Used for comparing media mix strategies, budget allocation analysis, and informing media planning decisions. | :ui-name:COMMSPOINT Media Mix Strategies :short-name:commspoint_mix |<

## Data Dictionary

### Fields:

- `mix_type` (STRING): Identifier for the media mix strategy or scenario (e.g., 2025_baseline, balanced_reach, brand_impact, conversion_focused). Business purpose: groups channel allocations by strategy to enable strategy-level comparison and decision-making. Typical usage: filter and compare budget allocations across strategies, join to strategy metadata for objectives and planning context, and serve as a categorical dimension for reporting and analysis. | :lower |<
- `channel` (STRING): Human-readable name of the media or marketing channel being allocated budget (e.g., TV ads, AVOD ads, Facebook ads, Instagram ads). Business purpose: identifies the delivery vehicle where budget is allocated and performance metrics are measured. Typical usage: report and visualize channel-level allocations, drive media planning and budget allocation decisions, and join to channel master/lookup tables for standardized attributes. | :lower |<
- `channel_group` (STRING): Category or grouping of the media channel (e.g., Broadcast, Digital, Social network, Retail, Influence, Direct). Business purpose: provides hierarchical organization of channels for aggregated reporting and analysis. Typical usage: group and aggregate metrics by channel category, compare performance across channel groups, and inform strategic media mix decisions. | :lower |<
- `budget` (FLOAT): Monetary budget allocated to the channel within the specified mix strategy. Business purpose: quantifies the investment level for each channel to support budget allocation, optimization, and financial planning. Typical usage: sum budgets by mix_type or channel_group for total allocation analysis, compare budgets across strategies, and feed into optimization models.
- `grps` (FLOAT): Gross Rating Points (GRPs) achieved for the channel at the allocated budget level. Business purpose: measures the total audience exposure and reach-frequency impact of the channel investment. Typical usage: compare GRPs across channels and strategies, calculate total GRPs for reach planning, and assess efficiency (GRPs per dollar) for optimization.
- `impressions` (FLOAT): Estimated number of ad impressions delivered for the channel at the allocated budget level. Business purpose: quantifies the total number of times ads are displayed to measure scale and audience exposure. Typical usage: compare impression volumes across channels, calculate cost per impression (CPI), assess reach and frequency, and inform inventory planning.

## (OPTIONAL) Table Relationships

## (Optional) Business Context
This table combines multiple COMMSPOINT media mix scenarios to enable side-by-side comparison of different strategic approaches. Each mix_type represents a different optimization objective or planning scenario, allowing analysts to evaluate trade-offs between strategies.

## (Optional) Notes

