import font_styles, keyboard, time, pyperclip
from rich.console import Console 

"""
𝓬𝓾𝓻𝓼𝓲𝓿𝓮 𝓲𝓼 𝓵𝓲𝓴𝓮 𝓽𝓱𝓲𝓼
original is like this
14-21-13-2-5-18-19- -1-18-5- -12-9-11-5- -20-8-9-19
ⓑⓤⓑⓑⓛⓔ ⓘⓢ ⓛⓘⓚⓔ ⓣⓗⓘⓢ
ꜱᴛᴀᴍᴘᴇᴅ ɪꜱ ʟɪᴋᴇ ᴛʜɪꜱ
"""


dictionary1 = {
    'original': font_styles.original,
    'cursive': font_styles.font_style1,
    'numbers': font_styles.font_style2,
    'bubble': font_styles.font_style3,
    'stamped': font_styles.font_style4
}

def clipboard_monitor(recent_value):
    try:
        clipboard_content = pyperclip.paste()

        if clipboard_content and clipboard_content != recent_value:
            return clipboard_content
        return None
    except pyperclip.PyperclipException as e:
        print(f"Error: Could not read clipboard. Reason: {e}")
        return None


def check_segment(setting):
    console = Console()
    setting = setting.lower()
    if setting not in dictionary1:
        console.print("[bold red]Error, setting default to 'cursive'[/bold red]")
        setting = 'cursive'

    time.sleep(0.7)
    return setting

def letters_to_numbers_with_lists(highlight, setting):
    alphabet = dictionary1['original']
    changed = dictionary1[setting]

    converted_parts = []
    for character in highlight:
        if character in alphabet:
            index = alphabet.index(character)
            converted_parts.append(str(changed[index]))
        else:
            converted_parts.append(character)

    if setting == 'numbers':
        result = "-".join(converted_parts)
    else:
        result = "".join(converted_parts)


    return result

def type_out_style(string):
    keyboard.press_and_release("ctrl+a")
    keyboard.press_and_release('backspace')
    keyboard.write(string)


    