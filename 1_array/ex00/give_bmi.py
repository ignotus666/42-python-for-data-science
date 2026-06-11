
def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    Checks if height and weight lists are actually lists, and
    if values are ints or floats.
    Calculates the BMI for each weight/height pair and returns
    a list with these BMIs
    """
    assert isinstance(height, list) and isinstance(weight, list), \
        ("height and weight must be lists!")
    assert len(height) == len(weight), \
        ("height and weight lists must be of equal length!")
    for item in height:
        assert type(item) in (int, float) and item > 0, \
            ("height must be higher than 0!")
    for item in weight:
        assert type(item) in (int, float) and item >= 0, \
            ("weight can't be negative!")

    bmi_list = []
    for h, w in zip(height, weight):
        bmi = w / (h * h)
        bmi_list.append(bmi)
    return (bmi_list)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Receives a list of BMIs and a limit. Returns a list of bools
    stating whether each BMI is over the limit (true) or not (false)
    """
    assert isinstance(bmi, list), "argument not a list!"
    for item in bmi:
        assert isinstance(item, (int, float)), ("list items"
                                                "are of the wrong type!")
    assert isinstance(limit, int), ("limit must be an int!")
    limit_list = []
    for value in bmi:
        limit_list.append(value > limit)
    return (limit_list)
