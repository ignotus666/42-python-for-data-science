import numpy


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    assert len(height) == len(weight)
    for item in height:
        assert isinstance(item, (int, float)), "AssertionError"
    for item in weight:
        assert isinstance(item, (int, float)), "AssertionError"

    bmi_list = []
    for h, w in zip(height, weight):
        bmi = h / (w * w)
        bmi_list.append(bmi)
    return (bmi_list)

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]: