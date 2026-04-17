import typer
import pyfiglet
from enum import Enum
from rich.text import Text
from rich.panel import Panel
from InquirerPy import inquirer
from rich.console import Console

console = Console()

class Status(str, Enum):
    APPLIED = 'Applied'
    INTERVIEWING = 'Interviewing'
    OFFER = 'Offer'
    REJECTED = 'Rejected'
    WITHDRAWN = 'Withdrawn'
    GHOSTED = 'Ghosted'
    ACCEPTED = 'Accepted'

class JobType(str, Enum):
    FULL_TIME = 'Full-time'
    PART_TIME = 'Part-time'
    INTERNSHIP = 'Internship'
    CONTRACT = 'Contract'
    FREELANCE = 'Freelance'

def show_menu():
    menu = inquirer.select(
        message = "Select an action:",
        qmark='',
        amark='',
        choices = ['Add Job', 'View Jobs', 'Update Job', 'Delete Job', 'Generate Sankey Graph', 'Exit'],
        border = True
    ).execute()
    return menu

def show_banner():
    # Text definitions
    welcomeText = pyfiglet.figlet_format("JOB TRACKER CLI", font="standard", width=100).rstrip()
    coloredText = Panel(welcomeText, style="bold yellow")
    authorText = Text("by: github.com/natetann", style="bold underline magenta")

    # Rich text prints
    console.print(coloredText, justify="center")
    console.print(authorText, justify="center")

def prompt_status():
    status = inquirer.select(
        message = 'Status:',
        qmark='',
        amark='',
        choices = [status.value for status in Status],
        default = Status.APPLIED.value
    ).execute()
    return status

def prompt_type():
    type = inquirer.select(
        message = 'Job type:',
        qmark='',
        amark='',
        choices = [job_type.value for job_type in JobType],
        default = JobType.FULL_TIME.value
    ).execute()
    return type

def prompt_job_details():
    title = typer.prompt('Job title', type=str)
    company = typer.prompt('Company', type=str)
    location = typer.prompt('Location', type=str)
    type = prompt_type();
    status = prompt_status();
    return title, company, location, type, status

def show_text(operation: str, type: str):
    if type == 'success':
        richText = Panel(operation, style="bold green")
        console.print(richText)
    elif type == 'error':
        richText = Panel(operation, style="bold red")
        console.print(richText)
    elif type == 'info':
        richText = Panel(operation, style="bold blue")
        console.print(richText)
