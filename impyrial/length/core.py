from ..utils import helper_function

UNITS = ("in", "ft", "yd")

def inches_to_feet(x, reverse=False):
    print(f"Test imports: {helper_function(x)}")
    if reverse:
        return x * 12
    return x / 12


def inches_to_yards(x, reverse=False):
    if reverse:
        return x * 36
    return x / 36

inches_to_feet(3)