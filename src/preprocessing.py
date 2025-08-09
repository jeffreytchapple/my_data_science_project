import pandas as pd
from sklearn.preprocessing import StandardScaler

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Performs basic preprocessing like filling missing values and encoding.
    """
    df = df.copy()
    
    # Drop duplicates
    df = df.drop_duplicates()
    
    df = df.dropna().reset_index(drop=True)
    # print("\nDataFrame after dropping rows with any NaN:")
    # print(df_cleaned_rows)
    
    # Fill missing numeric values with median
    numeric_cols = df.select_dtypes(include="number").columns
    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].median())
    
    # Fill missing categorical values with mode (if any non-empty)
    categorical_cols = df.select_dtypes(include="object").columns
    for col in categorical_cols:
        if not df[col].mode().empty:
            df[col] = df[col].fillna(df[col].mode()[0])
        else:
            df[col] = df[col].fillna("")
        
    """
    this code adds a bunch of true and false columns I 
    am not sure what they are...
    """
    
    # One-hot encode categoricals
    # df = pd.get_dummies(df, drop_first=True)
    return df
