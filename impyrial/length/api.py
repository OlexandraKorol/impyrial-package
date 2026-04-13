("in", "ft", "yd")

from .core import inches_to_feet, inches_to_yards, UNITS
from ..utils import convert_to_meters


def convert_unit(x, from_unit, to_unit):
    if from_unit not in UNITS or to_unit not in UNITS:
        raise ValueError("Unsupported unit, please choose from: in, ft, yd")

    if from_unit == "ft":
        x = inches_to_feet(x, reverse=True)
    elif from_unit == "yd":
        x = inches_to_yards(x, reverse=True)

    if to_unit == "ft":
        return inches_to_feet(x)
    elif to_unit == "yd":
        return inches_to_yards(x)
    elif to_unit == "in":
        return x
    elif to_unit == "m":
        return convert_to_meters(x)