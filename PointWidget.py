import yaml
import tkinter as tk
from TrackWidgetBase import Coord, TrackWidgetBase, SCALE


class PointWidget(TrackWidgetBase):
    def __init__(self, *, ori, height, width, **placement):
        super().__init__(ori=ori, width=width, height=height, **placement)

    def idle_xy (self, x_or_y : int) -> int:
        return x_or_y

    def mirror_x(self, x : int) -> int:
        return self.width - x

    def mirror_y(self, y : int) -> int:
        return self.height - y

    def mk_coords(self, func_x, func_y):
        self.pa = Coord(func_x(0), func_y(self.height-10))
        self.pb = Coord(func_x(self.width), func_y(self.height-10))
        self.p = Coord(func_x(self.length_legA), func_y(self.height-10))
        if self.width - self.length_legA > self.height - 10:
            # connector C at top/bottom
            self.pc = Coord(func_x(self.length_legA + self.height - 10), func_y(0))
        else:
            # connector C at left/right
            self.pc = Coord(func_x(self.width), func_y(self.height - 10 - self.width + self.length_legA))

    def create_widget(self, name, master_frame, gui):
        TrackWidgetBase.create_widget(self, name, master_frame, gui)
        self.length_legA = self.placement.get('length_legA', self.width-self.height+20)
#        self.canvas.configure(bg='gray65')

        if self.ori == 'ne':
            self.mk_coords(self.idle_xy, self.idle_xy)
            text_y_default = self.height - 4
        if self.ori == 'nw':
            self.mk_coords(self.mirror_x, self.idle_xy)
            text_y_default = self.height - 4
        if self.ori == 'se':
            self.mk_coords(self.idle_xy, self.mirror_y)
            text_y_default = 4
        if self.ori == 'sw':
            self.mk_coords(self.mirror_x, self.mirror_y)
            text_y_default = 4

        pa = self.pa
        pb = self.pb
        p = self.p
        pc = self.pc

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
