import logging

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

