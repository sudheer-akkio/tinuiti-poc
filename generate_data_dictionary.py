import os
import sys
from pathlib import Path
import pandas as pd
import numpy as np

# Add the parent directory to the path so we can import from src
sys.path.append(str(Path(__file__).parent))
sys.path.append(str(Path(__file__).parent / 'data-warehouse-sdk'))

from src.data_dictionary.DataDictionaryManager import DataDictionaryManager
from src.utils import load_data_file, generate_table_name

root_path = Path(__file__).parent

schema_path = root_path / 'data_schemas'

data_path = root_path / "data"

files = [str(data_path / f) for f in os.listdir(str(data_path)) if f.endswith('.csv')]

for file in files:

    print(f"Generating data dictionary for {file}")

    data_sample = load_data_file(file, read_chunk_size=10000)

    table_name = file.split('/')[-1].split('.')[0]

    # Initialize DataDictionaryManager with sample data
    manager = DataDictionaryManager(
        data_dictionary_path=schema_path,
        data_sample=data_sample
    )

    results = manager.generate_data_dictionary(table_name=table_name)