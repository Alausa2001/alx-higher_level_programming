"""when doctest sees the headline 'Traceback (most recent call last)' or
'Traceback (innermost last) it ignores the body of the Traceback and skips ahead to find the exception
"""
def raises():
    """
    >>> raises()
    Traceback (most recent call last):
    ValueError: here is an error
    """
    raise ValueError("here is an error")
