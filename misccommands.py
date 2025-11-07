from rich.console import Console
import os

console = Console()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def info_command():
    console.rule(style="bold blue")
    console.print("[bold blue]=== INFO OF ALL COMMANDS===[/bold blue]\n[green]'info' = List of commands\n'start' = Starts machine\n'exit' = Basically exiting the machine, what else?[/green]")
    console.input("Press [yellow]'enter'[/yellow] to return menu...")

def select_style():
    console.rule(style="bold yellow")
    console.print("[bold cyan]Type in any setting you want[/bold cyan]\n\n[green]* Cursive\n* Numbers\n* Bubble\n* Stamped[/green]\n[bold red]* Exit[/bold red]\n")
