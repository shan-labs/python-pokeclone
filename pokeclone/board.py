class Cell:
    def __init__(self, on = None):
        self.on = on

    def __str__(self):
        return self.on if self.on else "x"

class Board:
    def __init__(self, l, w):
        self.l = l
        self.w = w
        self.grid = [[Cell() for _ in range(w)] for _ in range(l)]
        self.px = 0
        self.py = 0
        self.grid[self.px][self.py] = Cell("P")

    def __str__(self):
        display = ""
        border = "-" * (self.w * 2 + 3) + "\n"

        display += border
        for row in self.grid:
            display += "| "
            for col in row:
                display += str(col) + " "
            display += "|\n"
        display += border

        return display

    def update_player_pos(self, offset):
        [ro, co] = offset
        newx = self.px + ro
        newy = self.py + co
        if newx < 0 or newx >= self.l or newy < 0 or newy >= self.w:
            return False

        self.grid[self.px][self.py] = Cell()
        self.px = newx
        self.py = newy
        self.grid[self.px][self.py] = Cell("P")

        return True
