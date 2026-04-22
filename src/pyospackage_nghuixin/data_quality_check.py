def count_missing(values):
    """
    Count None values in a list.
    """
    return sum(v is None for v in values)


def find_duplicates(values):
    """
    Return duplicate values in a list.
    """
    seen = set()
    duplicates = set()

    for v in values:
        if v in seen:
            duplicates.add(v)
        else:
            seen.add(v)

    return list(duplicates)


def check_required_keys(record, required_keys):
    """
    Check if a dictionary has all required keys.
    """
    return [key for key in required_keys if key not in record]