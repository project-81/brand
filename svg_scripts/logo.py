"""
A script for generating the project-81 logo.
"""

# built-in
from typing import List

# third-party
from svgen.attribute.viewbox import ViewBox
from svgen.element import Element


def compose(viewbox: ViewBox, config: dict) -> List[Element]:
    """An example function for composing a document."""

    print(viewbox)
    print(config)
    return []
