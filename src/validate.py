import pandas as pd


def ValidateDataframe(df: pd.DataFrame, non_negative_cols=None, required_cols=None, unique_key_cols=None):
    if non_negative_cols:
        for col in non_negative_cols:
            assert col in df.columns, f"column '{col}' not found in DataFrame"
            assert (df[col] >= 0).all(), f"'{col}' contains negative values"

    if required_cols:
        for col in required_cols:
            assert col in df.columns, f"required column '{col}' not found in DataFrame"
            assert df[col].notna().all(), f"'{col}' contains null values"

    if unique_key_cols:
        assert all(c in df.columns for c in unique_key_cols), f"one or more key columns {unique_key_cols} not found in DataFrame"
        assert df.duplicated(subset=unique_key_cols).sum() == 0, f"duplicate keys found on columns {unique_key_cols}"
