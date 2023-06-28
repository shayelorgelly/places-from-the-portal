import os
import recolor
import sys
import time

defaultDelay = 35  # ms
# defaultDelay = 0  # for testing purposes
white = [255, 255, 255]


def sleep(ms: int):  # in milliseconds
    time.sleep(ms / 1000)


wait, delay = sleep, sleep  # alias


def type_writer(text: str, delay_between_char: int):
    """using type hints because I like type hints"""
    assert text, "text missing"
    if not delay_between_char:
        delay_between_char = defaultDelay
    for char in text:
        sys.stdout.write(char)
        sleep(delay_between_char)


def clear_console():
    sys.stdout.write("\033c")


def type_writer_color(text: str, color, delay_between_char: int):
    assert text, "text missing"  # make sure we have it
    assert color, "color missing..."
    if not delay_between_char:
        delay_between_char = defaultDelay
    for char in text:
        # for every character in the string
        sleep(delay_between_char)
        sys.stdout.write(recolor.color_text(char, color))
        sys.stdout.flush()


def jstypec(words: str, color, delay_between_words: int):  # john smith type
    type_writer_color("John Smith: ", [255, 200, 0], defaultDelay)
    type_writer_color(words, color, delay_between_words)


def match_from_array(data: str, array) -> bool:
    """cant figure out how to use type hints for array."""
    out = False
    for x in array:
        if x == data:
            out = True
    if out:
        return True
    else:
        return False


def clear():
    os.system("cls")
    # print("\033c")
