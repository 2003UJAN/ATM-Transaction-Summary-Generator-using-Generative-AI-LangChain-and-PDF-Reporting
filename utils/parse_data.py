# utils/parse_data.py

import pandas as pd

def load_transaction_data(file_path):
    """
    Load ATM transaction log CSV into a pandas DataFrame.
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        raise ValueError(f"Error loading CSV: {e}")
