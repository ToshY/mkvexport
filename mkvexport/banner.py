import pyfiglet  # type: ignore
from rich import print


def cli_banner(
    banner_title: str,
    banner_font: str = "standard",
    banner_color: str = "yellow",
    banner_width: int = 200,
) -> None:
    """
    Print out the banner
    """

    banner = pyfiglet.figlet_format(banner_title, font=banner_font, width=banner_width)
    print(f"[{banner_color}]{banner}[/{banner_color}]")
