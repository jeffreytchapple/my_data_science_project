import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Performs basic preprocessing like filling missing values and encoding.
    """
    df = df.copy()

    # Fill missing numeric values with median
    numeric_cols = df.select_dtypes(include="number").columns
    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].median())

    # Fill missing categorical values with mode
    categorical_cols = df.select_dtypes(include="object").columns
    for col in categorical_cols:
        df[col] = df[col].fillna(df[col].mode()[0])

    # Encode categorical columns
    df = pd.get_dummies(df, drop_first=True)

    return df
