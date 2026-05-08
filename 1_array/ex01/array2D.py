import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Takes a 2D array (list), a start and an end.
    Checks if it's actually a list, and whether start and
    end are ints. Checks if the rows have equal lengths.
    Then it converts the list into a numpy array and slices it
    according to start and end. Prints the before/after shapes.
    Returns:
            Sliced array converted back into a list.
    """
    try:
        if not isinstance(family, list):
            raise TypeError("family must be a list")
        if not isinstance(start, int) or not isinstance(end, int):
            raise TypeError("start and end must be ints")

        row_len = len(family[0]) if family else 0
        if family and not all(isinstance(row, (list, tuple))
                              and len(row) == row_len for row in family):
            raise ValueError("all rows must have the same length")

        arr = np.array(family)
        print(f"My shape is : {arr.shape}")

        sliced = arr[start:end]
        print(f"My new shape is : {sliced.shape}")

        return sliced.tolist()

    except AssertionError as e:
        print("AssertionError:", e)
    except Exception as e:
        print("Exception:", e)
