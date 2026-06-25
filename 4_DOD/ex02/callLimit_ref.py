from typing import Any


def callLimit(limit: int):
    """Decorator factory that enforces a maximum call count on a function.
    Uses a closure to remember `limit` and a decorator.

    Creates a three-layer closure:
      - callLimit(limit): a decorator factory, creates (returns) the decorator.
      - callLimiter(function): the decorator, wraps the target function.
      - limit_function(*args, **kwds): the wrapper.

    Args:
        limit: Maximum number of times the wrapped function may be called.

    Returns:
        The callLimiter decorator: takes a function and returns a wrapper.
    """

    if not isinstance(limit, int):
        raise TypeError(f"limit must be int, got {type(limit)}")

    def callLimiter(function):
        """Decorator that wraps `function` with a call counter and limit.

        Args:
            function: The function to wrap.

        Returns:
            A wrapper function that counts calls and enforces `limit`.
        """

        count = 0

        if not callable(function):
            raise TypeError(f"function must be callable, got {type(function)}")

        def limit_function(*args: Any, **kwds: Any):
            """
            Wrapper that calls the wrapped function, enforcing the call limit.

            Args:
                *args: Positional arguments passed to the wrapped function.
                **kwds: Keyword arguments passed to the wrapped function.

            Returns:
                The result of the wrapped function, or None if the limit
                has been exceeded.
            """

            nonlocal count
            count += 1

            if count > limit:
                print(f"Error: {function} call too many times")
                return None
            return function(*args, **kwds)

        return limit_function

    return callLimiter
