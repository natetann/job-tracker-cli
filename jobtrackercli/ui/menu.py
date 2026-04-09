from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from InquirerPy import inquirer

def show_menu():
    menu = inquirer.select(
        message = "Select an action:",
        choices = ['Add Job', 'View Jobs', 'Update Job', 'Delete Job', 'Generate Sankey Graph', 'Exit'],
        border = True
    ).execute()
    return menu