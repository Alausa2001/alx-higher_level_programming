
"""There are cases where the unpredictable value cannot be ignored, because that would make the test incomplete or inaccurate. 
For example, simple tests quickly become more complex when dealing with data types whose string representations are inconsistent. for example forming a set from a list"""
def example(b=[]):
    """
    >>> c = [1, 22, 3, 55, 6, 90]
    >>> example(c)
    {1, 3, 6, 22, 55, 90}
    """
    sett = set(sorted(b))
    return sett
