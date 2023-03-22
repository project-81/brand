"""
A module for drawing a compass graphic.
"""

# built-in
from typing import List

# third-party
from svgen.attribute import SimpleAttribute
from svgen.cartesian.rectangle import Rectangle
from svgen.element import Element
from svgen.element.circle import Circle


def add_compass(box: Rectangle, scale: float = 1.0) -> List[Element]:
    """
    Return elements composing a compass graphic centered inside the provided
    rectangle.
    """

    border = Circle.centered(
        box, radius_scale=scale, color="white", prop="stroke"
    )

    # make this simpler, fix typing issue
    border.add_attribute(
        SimpleAttribute("stroke-width", border.raw.radius / 9)  # type: ignore
    )

    return [border]
