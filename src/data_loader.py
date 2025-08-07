import os
import pandas as pd
from dotenv import load_dotenv

# Load .env variables
load_dotenv()
DATA_PATH = os.getenv("DATA_PATH", "./data")

def load_data(filename: str, subfolder: str = "raw") -> pd.DataFrame:
    """
    Loads a CSV file from the specified subfolder within the data directory.
    """
    path = os.path.join(DATA_PATH, subfolder, filename)
    try:
        df = pd.read_csv(path)
        print(f"Loaded {len(df)} records from {path}")
        return df
    except FileNotFoundError:
        print(f"File not found: {path}")
        return pd.DataFrame()
