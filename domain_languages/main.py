from typing import Optional

from turtle_graphics_parser import parser
from turtle_graphics_drawer import TurtleGraphicsDrawer


drawer = TurtleGraphicsDrawer()


def input_reader(command: str, operand: Optional[int]):

    parsed_command: str = parser(command)
    if operand is None:
        getattr(TurtleGraphicsDrawer, parsed_command)(drawer)
    else:
        getattr(TurtleGraphicsDrawer, parsed_command)(drawer, operand)


def main():
    commands = [
        ("P", 2),
        ("D", None),
        ("W", 2),
        ("N", 1),
        ("E", 2),
        ("S", 1),
        ("U", None)
    ]
    for command, operand in commands:
        input_reader(command, operand)


if __name__ == '__main__':
    main()
