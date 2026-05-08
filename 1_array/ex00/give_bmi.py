
def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    assert isinstance(height, list) and isinstance(weight, list)
    assert len(height) == len(weight)
    for item in height:
        assert isinstance(item, (int, float)), "AssertionError"
    for item in weight:
        assert isinstance(item, (int, float)), "AssertionError"

    bmi_list = []
    for h, w in zip(height, weight):
        bmi = w / (h * h)
        bmi_list.append(bmi)
    return (bmi_list)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    for item in bmi:
        assert isinstance(item, (int, float)), "AssertionError"
    assert isinstance(limit, int)
    limit_list = []
    for value in bmi:
        limit_list.append(value > limit)
    return (limit_list)
