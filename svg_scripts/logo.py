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


def compose(viewbox: ViewBox, config: dict) -> List[Element]:
    """An example function for composing a document."""

    # Register color palettes.
    register_colors(COLORS_ROOT)

    chip_elems, _ = add_chip(viewbox.box, circle_color=config["circle_color"])

    return chip_elems
