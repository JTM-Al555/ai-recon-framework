from rich.console import Console
from rich.panel import Panel


console = Console()


def show_banner():

    banner = r"""
      ___    ___      _____
     /   |  /   |    / ___/___  ______
    / /| | / /| |    \__ \/ _ \/ ___/
   / ___ |/ ___ |   ___/ /  __/ /
  /_/  |_/_/  |_|  /____/\___/_/

      AI-Powered Recon Framework
    """

    console.print(
        Panel.fit(
            banner,
            border_style="cyan"
        )
    )