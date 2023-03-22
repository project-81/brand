"""
A script for generating the project-81 logo.
"""

# built-in
from typing import List

# third-party
from svgen.attribute.viewbox import ViewBox
from svgen.element import Element
from svgen.shapes.chip import add_chip

# internal
from svg_scripts import COLORS_ROOT
from svg_scripts.lib import register_colors
from svg_scripts.lib.compass import add_compass


def compose(viewbox: ViewBox, config: dict) -> List[Element]:
    """An example function for composing a document."""

    # Register color palettes.
    register_colors(COLORS_ROOT)

    chip_elems, rect = add_chip(
        viewbox.box, circle_color=config["circle_color"]
    )

    chip_elems += add_compass(rect.rect, scale=2 / 3)

    return chip_elems
