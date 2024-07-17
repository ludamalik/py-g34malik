from rich.prompt import Prompt
from rich import print as rprint
from todo import __app_name__, __version__
import typer
from typing import Any

from todo.model import Todo

def make_title(fn: Any) -> Any:
    """This decorator function is a higher order function that take a function as parameter."""

    def wrapper() -> Any:
        func = fn()
        output = func.title()
        return output
    return wrapper

@make_title
def add_your_task() -> str:
    return Prompt.ask("[bold green on blue] Text Your task [/]", default='Todo somethig else')

def join_category() -> str:
    res = ''
    for k, v in Todo.COLORS.items():
        res += f"[bold white on {v}] {k} [/]"
    return res

@make_title
def choose_category() -> str:
    return Prompt.ask("[bold green on blue] Choose category [/]" + join_category(), default='Work')

def hello() -> None:
    rprint(F"[bold magenta]{__app_name__.upper()}[/bold magenta]", chr(128187), F"[bold magenta]{__version__}[/bold magenta]")

def make_your_choice() -> str:
    return Prompt.ask("[bold green on blue] Make Your Choice (a|l|u|r|q) [/]")

def bye(TITLE: str) -> None:
    typer.secho(f"Thanks for using {TITLE}. Have a nice day!", fg=typer.colors.BRIGHT_GREEN)

def help_me() -> None:
    typer.secho("""
    All that You can do:      
        l : List existing contacts
        a : Add new contact
        u : Update existing contact
        r : Remove existing contact
        h : Print this help
        q : Exit
    """, fg=typer.colors.BRIGHT_GREEN, bg=typer.colors.BRIGHT_WHITE)
