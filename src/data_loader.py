import os
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv

# Load .env variables (if present)
load_dotenv()

def get_project_root() -> Path:
    """
    Return the absolute path to the project root.
    Assumes this file lives at <project_root>/src/data_loader.py
    """
    return Path(__file__).resolve().parents[1]

def load_data(filename: str, subfolder: str = "raw") -> pd.DataFrame:
    """
    Loads a CSV file from the specified subfolder within the data directory.
    Works in Jupyter notebooks regardless of current working directory.
    """
    # Resolve DATA_PATH from .env or default to <project_root>/data
    data_path_env = os.getenv("DATA_PATH")
    if data_path_env:
        data_path = Path(data_path_env).expanduser().resolve()
    else:
        data_path = get_project_root() / "data"

    path = data_path / subfolder / filename

    try:
        df = pd.read_csv(path)
        print(f"Loaded {len(df)} records from {path}")
        return df
    except FileNotFoundError:
        print(f"File not found: {path}")
        return pd.DataFrame()
