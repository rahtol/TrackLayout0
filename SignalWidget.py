import yaml
import tkinter as tk
from TrackWidgetBase import Coord, TrackWidgetBase, SCALE


class SignalWidget(TrackWidgetBase):
    def __init__(self, *, ori, height, width, **placement):
        super().__init__(ori=ori, width=width, height=height, **placement)

    def create_widget(self, name, master_frame, gui):
        TrackWidgetBase.create_widget(self, name, master_frame, gui)
#        self.canvas.configure(bg='gray85')

        # west/east: where the baseline is located, i.e. left/right box boundary
        # north/south: signal located above or below track, i.e. at lower/upper box boundary
        # minimum size of signal with two bulbs 11x32px without text or 20x32px with text
        # the create_oval bounding box includes the (x1,y1) coordinate ???
        if self.ori == 'sw':
            self.p1 = Coord(4, 5)
            self.dx = 10
        elif self.ori == 'se':
            w = self.width-1
            self.baseline = self.canvas.create_line(w-1, 1, w-1, 10, width=3)
            self.pole = self.canvas.create_line(w-1, 5, w-10, 5, width=3)
            self.light1 = self.canvas.create_oval(w-10, 0, w-20, 10, outline='', fill='blue')
            self.light2 = self.canvas.create_oval(w-21, 0, w-31, 10, outline='', fill='yellow')
            self.text_x = self.placement.get('text_x', self.width)
            self.text_y = self.placement.get('text_y', self.height + 1)
            self.text_anchor = self.placement.get('text_anchor', 'se')
        elif self.ori == 'nw':
            self.baseline = self.canvas.create_line(1, 10, 1, 19, width=3)
            self.pole = self.canvas.create_line(1, 14, 10, 14, width=3)
            self.light1 = self.canvas.create_oval(10, 9, 20, 19, outline='', fill='red')
            self.light2 = self.canvas.create_oval(21, 9, 31, 19, outline='', fill='green')
            self.text_x = self.placement.get('text_x', 0)
            self.text_y = self.placement.get('text_y', -2)
            self.text_anchor = self.placement.get('text_anchor', 'nw')
        elif self.ori == 'ne':
            self.p1 = Coord(self.width - 4, 15)
            self.dx = -10

        self.canvas.create_text(self.text_x, self.text_y, text=self.name, font=('Helvetica', 6),
                                anchor=self.text_anchor)


def SignalWidget_constructor(loader: yaml.SafeLoader, node: yaml.nodes.MappingNode) -> SignalWidget:
    return SignalWidget(**loader.construct_mapping(node))
