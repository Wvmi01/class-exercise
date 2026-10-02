import logging

import re #class7
import pandas as pd

logger = logging.getLogger(__name__)

def show_overview(df):
    """Display basic information about a DataFrame."""
    logger.debug(f"loading file information")
    print(df.shape)
    print(df.head())
    print("Columns:")
    print(list(df.columns))
    print("Data types:")
    print(df.dtypes)

def remove_duplicates(df):
    """Remove exact duplicate rows."""
    before = len(df)
    df = df.drop_duplicates()
    logger.debug(f"Removed {before - len(df)} duplicate row(s)")
    return df

def drop_missing_rows(df):
    """Remove rows containing missing values."""
    before = len(df)
    df = df.dropna()

    logger.debug(f"Original row count: {before}. Missing values removed: {df}.")
    return df

#class7
def clean_text(value):
    """Normalize one text value."""
    value = value.strip()
    value = value.lower()
    value = re.sub(r"\s+", " ", value)
    return value


def remove_iqr_outliers(df, column, threshold):
    """Remove IQR outliers from one column."""
    if column not in df.columns:
        logger.error(f"Column not found: {column}")
        raise ValueError(f"Column not found: {column}")
    
# Calculate Q1, Q3, and IQR.
# Use threshold to calculate lower and upper bounds.
    before = len(df)

    q1 = df[column].quantile(0.25)
    q3 = df[column].quantile(0.75)
    iqr = q3 - q1

    lower = q1 - threshold * iqr
    upper = q3 + threshold * iqr

    df = df[(df[column] >= lower) & (df[column] <= upper)].copy()

    logger.debug(
        f"{column}: bounds [{lower}, {upper}]"
        f"removed {before - len(df)} row(s)"
    )

    return df

