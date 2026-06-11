import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Takes a 2D array (list), a start and an end.
    Checks if it's actually a list, and whether start and
    end are ints. Checks if the rows have equal lengths.
    Then it converts the list into a numpy array and slices it
    according to start and end. Prints the before/after shapes.
    Returns sliced array converted back into a list.
    """
    assert isinstance(family, list), "family must be a list"
    assert type(start) is int and type(end) is int, ("start and end must be "
                                                     "ints")

    if family:
        row_len = len(family[0])
    else:
        row_len = 0
    if family and not all(isinstance(row, (list, tuple))
                          and len(row) == row_len for row in family):
        raise ValueError("all rows must have the same length")

    arr = np.array(family)
    print(f"My shape is : {arr.shape}")

    sliced = arr[start:end]
    print(f"My new shape is : {sliced.shape}")

    return sliced.tolist()
