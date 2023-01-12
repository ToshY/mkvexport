# pylint: disable=missing-module-docstring
import pyfiglet
from rich.console import Console

console = Console()


def cli_banner(
    banner_title: str,
    banner_font: str = "standard",
    banner_color: str = "#E85E00",
    banner_width: int = 200,
) -> None:
    """CLI banner"""

    banner = pyfiglet.figlet_format(banner_title, font=banner_font, width=banner_width)
    console.print(banner, style=banner_color)
