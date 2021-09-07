import yaml
import tkinter as tk
from TrackWidgetBase import Coord, TrackWidgetBase, SCALE


class SignalWidget(TrackWidgetBase):
    def __init__(self, *, ori, height, width, **placement):
        super().__init__(ori=ori, width=width, height=height, **placement)

    def create_widget(self, name, master_frame, gui):
        TrackWidgetBase.create_widget(self, name, master_frame, gui)
        self.canvas.configure(bg='gray85')

        # west/east: where the baseline is located, i.e. left/right box boundary
        # north/south: signal located above or below track, i.e. at lower/upper box boundary
        if self.ori == 'sw':
            self.p1 = Coord(4, 5)
            self.dx = 10
        elif self.ori == 'se':
            self.p1 = Coord(self.width - 2, 5)
            self.dx = -10
            self.text_x = self.placement.get('text_x', self.width)
            self.text_y = self.placement.get('text_y', self.height+1)
            self.text_anchor = self.placement.get('text_anchor', 'se')
        elif self.ori == 'nw':
            self.p1 = Coord(1, 14)
            self.dx = 10
            self.text_x = self.placement.get('text_x', 0)
            self.text_y = self.placement.get('text_y', -2)
            self.text_anchor = self.placement.get('text_anchor', 'nw')
        elif self.ori == 'ne':
            self.p1 = Coord(self.width - 4, 15)
            self.dx = -10

        self.baseline = self.canvas.create_line(self.p1.x, self.p1.y - 4, self.p1.x, self.p1.y + 5, width=3)
        self.pole = self.canvas.create_line(self.p1.x, self.p1.y, self.p1.x + self.dx, self.p1.y, width=3)
        self.light1 = self.canvas.create_oval(self.p1.x + 0.9 * self.dx, self.p1.y - 5, self.p1.x + 1.9 * self.dx,
                                              self.p1.y + 5)
        self.light2 = self.canvas.create_oval(self.p1.x + 1.9 * self.dx, self.p1.y - 5, self.p1.x + 2.9 * self.dx,
                                              self.p1.y + 5)
        self.canvas.create_text(self.text_x, self.text_y, text=self.name, font=('Helvetica', 6),
                                anchor=self.text_anchor)


def SignalWidget_constructor(loader: yaml.SafeLoader, node: yaml.nodes.MappingNode) -> SignalWidget:
    return SignalWidget(**loader.construct_mapping(node))
