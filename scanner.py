"""Made by Shaye Lorgelly"""
from functions import type_writer_color, sleep, defaultDelay


def scan(creature_name: str):
    type_writer_color("Scanning Creature", [255, 255, 0], defaultDelay * 2)
    type_writer_color("......\n", [255, 255, 0], 750)  # 750 milliseconds
    sleep(1000)
    type_writer_color("....Scanner Results.....\n", [150, 0, 255], defaultDelay * 2)
    type_writer_color("Species: ", [255, 255, 255], defaultDelay * 2)
    type_writer_color("       " + creature_name, [255, 255, 255], defaultDelay * 2)
    print("\n")
    type_writer_color("Hostile", [255, 0, 0], defaultDelay * 2)
    print("\n")
