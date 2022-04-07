

class TurtleGraphicsDrawer:

    pen_id = -1

    def __init__(self):
        print("Drawer initialized, please select a pen...")

    def select_pen(self, pen_id: int):
        self.pen_id = pen_id
        print(f"pen {self.pen_id} selected!")

    def pen_down(self):
        print(f"Pen {self.pen_id} down, ready to draw!")

    def pen_up(self):
        print(f"Pen {self.pen_id} up, done drawing")

    def draw_north(self, distance: int):
        self.console_draw(distance, "North")

    def draw_south(self, distance: int):
        self.console_draw(distance, "South")

    def draw_east(self, distance: int):
        self.console_draw(distance, "East")

    def draw_west(self, distance: int):
        self.console_draw(distance, "West")

    def console_draw(self, distance: int, direction: str):
        print(f"Pen {self.pen_id} draws {distance}cm {direction}")
