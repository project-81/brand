"""
Utility methods usable by any generator script.
"""

# built-in
from pathlib import Path

# third-party
from svgen.color.theme.manager import THEMES


def register_colors(colors_root: Path) -> None:
    """Register color palettes committed to this package."""

    THEMES.load_directory(colors_root)
