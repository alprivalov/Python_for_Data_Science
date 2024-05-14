def ft_filter(func, argv):
    """
filter(function or None, iterable) --> filter object
Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.
    """
    return [item for item in argv if func(item)]
