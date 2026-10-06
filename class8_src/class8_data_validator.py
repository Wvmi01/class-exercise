import logging

logger = logging.getLogger(__name__)


def require_columns(df, required_columns):
    """Check that all required columns exist."""
    # TODO 2:
    # Check if any of the configured columns (list) are missing from df.
    # If any are missing, log an ERROR and raise ValueError.
    # Log an INFO.
    # Return the DataFrame.
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        logger.error(f"Missing columns: {', '.join(missing_columns)}")
        raise ValueError(f"{len(missing_columns)} missing")
    logger.info(f"All required columns exist")
    return df


#    if df.column.isna():
#        logger.error(f"Column not found: {required_columns}")
#        raise ValueError(f"Column not found: {required_columns}")
#    logger.info(f"All required columns exist")
#    return df

# Won't give us a good idea of how many columns are missing:
# for col in require_columns:
# if col not in df.columns:
#    raise ValueError(f"Column {col} is missing")
