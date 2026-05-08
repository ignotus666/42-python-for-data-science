def ft_filter(function, iterable):
    """
    Filters a collection and returns a new list
    that meets a specific condition.
    - If a function is provided, it tests every item and
      only keeps those that the rule says are 'True'.
    - If no rule is provided (function is None), it removes
      anything 'empty' or 'zero' (like 0, None, or empty text).
    Parameters:
    - function: The rule used to test each item.
    - iterable: The collection of items to filter through.
    Returns:
    - A list of the items that pass the filter.
    """
    if function:
        return [item for item in iterable if function(item)]
    return [item for item in iterable if item]
