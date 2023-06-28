"""Color module made for the people using python."""


def color_text(message: str, rgb_array: list):
    """Add ansi color codes to the text and return string."""
    return f'\x1b[38;2;{";".join(map(str, rgb_array))}m{message}\x1b[0m'


def color_log(message: str, rgb_array: list):
    """Print message with color."""
    print(f'\x1b[38;2;{";".join(map(str, rgb_array))}m{message}\x1b[0m')


"""
import recolor
colorLog("hello", [0, 255, 0]) #green
colorText("Hello World!", [255, 0, 0]) #red
"""  # example usage


color_log("Colors Loaded :D", [255, 0, 0])
