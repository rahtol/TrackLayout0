import yaml
import tkinter as tk
from TrackWidgetBase import Coord, TrackWidgetBase, SCALE

ORI_ = 0
ORI_NW = 1
ORI_NE = 2
ORI_SW = 3
ORI_SE = 4




class PointWidget(tk.Canvas):
    def __init__(self, *, ori, height, width, **placement):
        self.ori = ori
        self.h = height / 10
        self.w = width / 10
        self.name = '???'
        self.placement = placement

    def create_widget(self, name, master_frame):
        self.name = name
        self.master_frame = master_frame
        tk.Canvas.__init__(self, self.master_frame, height=self.h * SCALE, width=self.w * SCALE, highlightthickness=0,
                           bg='gray75')

        if self.ori == 'ne':
            pa = Coord(0, (self.h - 1) * SCALE)
            pb = Coord(self.w * SCALE, (self.h - 1) * SCALE)
            pc = Coord(self.w * SCALE, 1 * SCALE)
            p = Coord((self.w - self.h + 2) * SCALE, (self.h - 1) * SCALE)
            text_y_default = self.h*SCALE-4
        if self.ori == 'nw':
            pa = Coord(self.w * SCALE, (self.h - 1) * SCALE)
            pb = Coord(0, (self.h - 1) * SCALE)
            pc = Coord(0, 1 * SCALE)
            p = Coord((self.h - 2) * SCALE, (self.h - 1) * SCALE)
            text_y_default = self.h*SCALE-4
        if self.ori == 'se':
            pa = Coord(0, 1 * SCALE)
            pc = Coord(self.w * SCALE, 1 * SCALE)
            pb = Coord(self.w * SCALE, (self.h - 1) * SCALE)
            p = Coord((self.w - self.h + 2) * SCALE, 1 * SCALE)
            text_y_default = 4
        if self.ori == 'sw':
            pa = Coord(self.w * SCALE, 1 * SCALE)
            pc = Coord(0, 1 * SCALE)
            pb = Coord(0, (self.h - 1) * SCALE)
            p = Coord((self.h - 2) * SCALE, 1 * SCALE)
            text_y_default = 4

        self.legA = self.create_line(pa.x, pa.y, p.x, p.y, width=4, fill='yellow', capstyle='butt')
        self.legB = self.create_line(p.x, p.y, pb.x, pb.y, width=4, fill='yellow', capstyle='butt')
        self.legC = self.create_line(p.x, p.y, pc.x, pc.y, width=4, fill='yellow', capstyle='butt')
        self.section_separatorA = self.create_line(pa.x, pa.y-4, pa.x, pa.y+4)
        self.section_separatorB = self.create_line(pb.x, pb.y-4, pb.x, pb.y+4)
        self.section_separatorC = self.create_line(pc.x, pc.y-4, pc.x, pc.y+4)

        self.text_x = self.placement.get('text_x', self.w*SCALE/2)
        self.text_y = self.placement.get('text_y', text_y_default)
        self.text_anchor = self.placement.get('text_anchor', 'center')

        self.create_text(self.text_x, self.text_y, text=self.name, font=('Helvetica', 6), anchor=self.text_anchor)

    def place_widget(self, display_widgets):
        if 'in_' in self.placement:
            # placement relative to another display_object using _in, anchor, relx, rely
            self.place(in_=display_widgets[self.placement['in_']],
                             **{k: v for k, v in self.placement.items() if k in ('anchor', 'relx', 'rely')})
        else:
            # placement using master frame coordinates
            self.place(**{k: v for k, v in self.placement.items() if k in ('x', 'y')})


def PointWidget_constructor(loader: yaml.SafeLoader, node: yaml.nodes.MappingNode) -> PointWidget:
    return PointWidget(**loader.construct_mapping(node))
