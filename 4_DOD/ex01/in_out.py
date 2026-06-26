def square(x: int | float) -> int | float:
    """Produce the square of the input"""
    return x ** 2


def pow(x: int | float) -> int | float:
    """Produces the input to the power of itself"""
    return x ** x


def outer(x: int | float, function) -> object:
    """
    Initialises the data and returns the inner function
    as an object.
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be an int or float")
    count = x

    def inner() -> float:
        """
        A closure is created by inner functions, where
        they will remember variables from the outer func.
        'nonlocal' ensures previous iterations of the var
        are modified and a new one isn't created each time.
        """
        nonlocal count

        count = function(count)
        return count

    return inner
