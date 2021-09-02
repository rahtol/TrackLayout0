import yaml
import tkinter as tk
from TrackWidgetBase import Coord, TrackWidgetBase, SCALE


class PointWidget(TrackWidgetBase):
    def __init__(self, *, ori, height, width, **placement):
        TrackWidgetBase.__init__(self, ori=ori, width=width, height=height, placement=placement)

    def create_widget(self, name, master_frame, gui):
        TrackWidgetBase.create_widget(self, name, master_frame, gui)
        tk.Frame.__init__(self, self.master_frame, height=self.height, width=self.width)
        self.canvas = tk.Canvas(self, height=self.height, width=self.width, highlightthickness=0, bg='gray75')
        self.bind('<Any-Enter>', self.mouse_enter)
        self.bind('<Any-Leave>', self.mouse_leave)

        if self.ori == 'ne':
            pa = Coord(0, self.height - SCALE)
            pb = Coord(self.width, self.height - SCALE)
            pc = Coord(self.width, SCALE)
            p = Coord(self.width - self.height + 2 * SCALE, self.height - SCALE)
            text_y_default = self.height - 4
        if self.ori == 'nw':
            pa = Coord(self.width, self.height - SCALE)
            pb = Coord(0, self.height - SCALE)
            pc = Coord(0, SCALE)
            p = Coord(self.height-2*SCALE, self.height - SCALE)
            text_y_default = self.height - 4
        if self.ori == 'se':
            pa = Coord(0, SCALE)
            pc = Coord(self.width, 1 * SCALE)
            pb = Coord(self.width, self.height - SCALE)
            p = Coord(self.width - self.height + 2 * SCALE, SCALE)
            text_y_default = 4
        if self.ori == 'sw':
            pa = Coord(self.width, SCALE)
            pc = Coord(0, 1 * SCALE)
            pb = Coord(0, self.height - SCALE)
            p = Coord(self.height - 2 * SCALE, SCALE)
            text_y_default = 4

        self.legA = self.canvas.create_line(pa.x, pa.y, p.x, p.y, width=4, fill='yellow', capstyle='butt')
        self.legB = self.canvas.create_line(p.x, p.y, pb.x, pb.y, width=4, fill='yellow', capstyle='butt')
        self.legC = self.canvas.create_line(p.x, p.y, pc.x, pc.y, width=4, fill='yellow', capstyle='butt')
        self.section_separatorA = self.canvas.create_line(pa.x, pa.y - 4, pa.x, pa.y + 4)
        self.section_separatorB = self.canvas.create_line(pb.x, pb.y - 4, pb.x, pb.y + 4)
        self.section_separatorC = self.canvas.create_line(pc.x, pc.y - 4, pc.x, pc.y + 4)

        self.text_x = self.placement.get('text_x', self.width / 2)
        self.text_y = self.placement.get('text_y', text_y_default)
        self.text_anchor = self.placement.get('text_anchor', 'center')

        self.canvas.create_text(self.text_x, self.text_y, text=self.name, font=('Helvetica', 6),
                                anchor=self.text_anchor)


def PointWidget_constructor(loader: yaml.SafeLoader, node: yaml.nodes.MappingNode) -> PointWidget:
    return PointWidget(**loader.construct_mapping(node))
