from typing import Any


def mean(data, data_len):
    """
    Mean calculated by adding values and dividing
    by number of them. No sorting needed.
    """
    mean_val = sum(data) / data_len
    return (mean_val)


def median(sorted_data, data_len):
    """
    Calculates median: if even number of items, return the
    mean of the middle two. If odd, return the middle one.
    Uses sorted list for ease of calclation.
    """
    if data_len % 2 == 1:
        median_val = sorted_data[data_len // 2]
    else:
        median_val = (sorted_data[(data_len // 2) - 1]
                      + sorted_data[data_len // 2]) / 2
    return (median_val)


def quartile(sorted_data, data_len):
    """
    Calculates quartile: using a sorted list, multiplying
    the list length by 0.25 and 0.75 gives you the indices
    corresponding to the 25% and 75% quartiles.
    """
    q1_val = float(sorted_data[int(data_len * 0.25)])
    q3_val = float(sorted_data[int(data_len * 0.75)])
    return ([q1_val, q3_val])


def var(data, data_len):
    """
    Calculates variance: average of the squared distance from the mean.
    """
    var_val = sum((x - mean(data, data_len)) ** 2 for x in data) / data_len
    return (var_val)


def std(data, data_len):
    """
    Calculates standard deviation: square root of the variance.
    """
    std_val = var(data, data_len) ** 0.5
    return (std_val)


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """
    Receives an arbitrary number of positional args and keyword args.
    Checks if positional args are numbers and if the value/s are among
    those there are methods for. If so, it calls the appropriate
    method/s and prints the result.
    """
    assert all(isinstance(vals, (int, float)) for vals in args), "ERROR"

    data = list(args)
    data_len = len(data)
    sorted_data = sorted(data)

    valid_ops = {"mean", "median", "quartile", "std", "var"}

    for value in kwargs.values():
        if value not in valid_ops:
            continue

        if data_len == 0:
            print("ERROR")
            continue

        if value == "mean":
            print(f"mean : {mean(data, data_len)}")

        elif value == "median":
            print(f"median : {median(sorted_data, data_len)}")

        elif value == "quartile":
            print(f"quartile : {quartile(sorted_data, data_len)}")

        elif value == "var":
            print(f"var : {var(data, data_len)}")

        elif value == "std":
            print(f"std : {std(data, data_len)}")
