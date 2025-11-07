import pyperclip, time, threading, keyboard, pyfiglet
from rich.console import Console

import mainFunctions, misccommands

stop_thread = False
console = Console()

def exit_program():
    global stop_thread
    console.print("[bold red]Shutting down...[/bold red]")
    stop_thread = True

def watch_for_exit():
    global stop_thread
    while not stop_thread:
        try:
            input_thing = input(">>> ").strip().lower()
            if input_thing == 'exit':
                console.rule(style="bold red")
                console.print("[red]Exit command received. Shutting down...[/red]")
                stop_thread = True
                break
        except (EOFError, KeyboardInterrupt):
            console.print("\n[yellow]Shutting down...[/yellow]")
            stop_thread = True
            break

def main_loop(setting):
    global stop_thread
    console.print("[bold green]Clipboard watcher started.[/bold green]")
    console.print("[italic yellow]Highlight and copy text to see it displayed as ASCII art.[/italic yellow]")
    console.rule(style="bold blue")
    time.sleep(1)

    input_thread = threading.Thread(target=watch_for_exit, daemon=True)
    input_thread.start()

    recent_value = ""
    try:
        while not stop_thread:
            new_content = mainFunctions.clipboard_monitor(recent_value)
            if new_content:
                misccommands.clear_screen()
                recent_value = new_content
                console.print("If you want to paste your work, use the hotkey 1+Q\nIf you want to leave, just type exit to end the script"
                              , style="bold yellow")
                console.rule(style="bold blue")
                console.print(f"[bold green]>>> New text detected on clipboard:[/bold green] [blue]'{recent_value}'[/blue]")
                try:
                    art = str(mainFunctions.letters_to_numbers_with_lists(recent_value.lower(), setting))
                    console.print(f"[bold green]>>> Converted string to:[/bold green]")
                    print(art)
                    console.rule(style="bold blue")
                    keyboard.add_hotkey('1+q', lambda: mainFunctions.type_out_style(art))
                except KeyboardInterrupt:
                    print("\nShutdown signal (Ctrl+C) received.")
                except pyperclip.PyperclipException as e:
                    console.print(f"Error: Could not render text. Reason: {e}")

            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\nShutdown signal (Ctrl+C) received.")
    finally:
        stop_thread = True
    console.print("[bold yellow]Exiting program.[/bold yellow]")

def main():
    global stop_thread
    while not stop_thread:
        misccommands.clear_screen()

        title = pyfiglet.figlet_format("Fatalist Typist", font='standard')
        console.print(title, style="bold orange1")
        console.rule(style="bold red")
        setting = console.input("[bold yellow]Type in commands (type help/info for commands):[/bold yellow] ")

        if setting == 'exit':
            exit_program()
        elif setting == 'help' or setting == 'info':
            misccommands.info_command()
        elif setting == 'start':
            misccommands.select_style()
            setting = console.input()

            if setting.lower() == 'exit':
                exit_program()
            else:
                setting = mainFunctions.check_segment(setting.lower())
                main_loop(setting)
        else:
            console.print("[bold red]Error. Try again.[/bold red]")
            time.sleep(1)

if __name__ == "__main__":
    main()

