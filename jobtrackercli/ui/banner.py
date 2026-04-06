from rich.console import Console
from rich.text import Text
from rich.panel import Panel
import pyfiglet

console = Console()

def show_banner():
    # Text definitions
    welcomeText = pyfiglet.figlet_format("JOB TRACKER CLI", font="standard", width=100).rstrip()
    coloredText = Panel(welcomeText, style="bold yellow")
    authorText = Text("by: github.com/natetann", style="bold underline magenta")

    # Rich text prints
    console.print(coloredText, justify="center")
    console.print(authorText, justify="center")