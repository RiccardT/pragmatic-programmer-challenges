

command_store: dict = {
    "P": "select_pen",
    "D": "pen_down",
    "W": "draw_west",
    "N": "draw_north",
    "E": "draw_east",
    "S": "draw_south",
    "U": "pen_up"
}


def parser(command: str) -> str:
    return command_store[command]


