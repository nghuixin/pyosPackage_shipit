def count_missing(values):
    """
    Count None values in a list.
    """
    return sum(v is None for v in values)

def missing_summary(df):
    """
    Return % missing per column.
    Relies on pandas library
    """
    return df.isnull().mean() * 100
