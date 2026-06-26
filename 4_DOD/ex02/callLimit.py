from typing import Any


def callLimit(limit: int):
    """
    Decorator factory. Limits how many times a decorated
    function can be run.
    Returns the callLimiter decorator function.
    """
    if type(limit) is not int:
        raise TypeError("Limit must be an int")
    count = 0

    def callLimiter(function):
        """
        Actual decorator. Receives the function and prepares
        it for wrapping.
        Returns the wrapped version of limit_function.
        """

        def limit_function(*args: Any, **kwds: Any):
            """
            Wrapper replacing the original function. Runs
            whenever the function is called. Checks if the
            limit has been reached and either returns an
            error or the value of the wrapped function.
            """
            nonlocal count

            if count >= limit:
                print(f"Error: {function} call too many times")
                return None
            else:
                count += 1
                return (function(*args, **kwds))

        return limit_function

    return callLimiter
