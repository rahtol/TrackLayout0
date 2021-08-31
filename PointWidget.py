import tkinter as tk

SCALE = 10
ORI_ = 0
ORI_NW = 1
ORI_NE = 2
ORI_SW = 3
ORI_SE = 4


class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class PointWidget(tk.Canvas):
    def __init__(self, master, name, *, ori, h, w):
        self.ori = ori
        self.h = h
        self.w = w
        self.name = name
        tk.Canvas.__init__(self, master, height=h * SCALE, width=w * SCALE, highlightthickness=0, bg='gray75')

        if self.ori == ORI_NE:
            pa = Coord(0, (self.h - 1) * SCALE)
            pb = Coord(self.w * SCALE, (self.h - 1) * SCALE)
            pc = Coord(self.w * SCALE, 1 * SCALE)
            p = Coord((self.w - self.h + 2) * SCALE, (self.h - 1) * SCALE)
        if self.ori == ORI_NW:
            pa = Coord(self.w * SCALE, (self.h - 1) * SCALE)
            pb = Coord(0, (self.h - 1) * SCALE)
            pc = Coord(0, 1 * SCALE)
            p = Coord((self.h - 2) * SCALE, (self.h - 1) * SCALE)
        if self.ori == ORI_SE:
            pa = Coord(0, 1 * SCALE)
            pc = Coord(self.w * SCALE, 1 * SCALE)
            pb = Coord(self.w * SCALE, (self.h - 1) * SCALE)
            p = Coord((self.w - self.h + 2) * SCALE, 1 * SCALE)
        if self.ori == ORI_SW:
            pa = Coord(self.w * SCALE, 1 * SCALE)
            pc = Coord(0, 1 * SCALE)
            pb = Coord(0, (self.h - 1) * SCALE)
            p = Coord((self.h - 2) * SCALE, 1 * SCALE)

        self.legA = super().create_line(pa.x, pa.y, p.x, p.y, width=3)
        self.legB = super().create_line(p.x, p.y, pb.x, pb.y, width=3)
        self.legC = super().create_line(p.x, p.y, pc.x, pc.y, width=3)
        super().create_text(3+10, 6, text=self.name, font=('Helvetica', 6))
