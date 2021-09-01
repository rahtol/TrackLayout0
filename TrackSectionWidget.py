import yaml
import tkinter as tk
from TrackWidgetBase import Coord, TrackWidgetBase, SCALE


class TrackSectionWidget(tk.Frame):
    def __init__(self, *, ori, width, height, **placement):
        self.ori = ori
        self.width = width
        self.height = height
        self.placement = placement

    def create_widget(self, name, master):
        self.name = name
        self.master_frame = master
        tk.Frame.__init__(self, self.master_frame, height=self.height, width=self.width)
        self.canvas = tk.Canvas(self, height=self.height, width=self.width, highlightthickness=0, bg='gray75')

        if self.ori == 'nw':
            self.p1 = Coord(0, SCALE)
            self.p2 = Coord(self.height-2*SCALE, self.height - SCALE)
            self.p3 = Coord(self.width, self.height - SCALE)
            text_y_default = self.height-4
        elif self.ori == 'ne':
            self.p1 = Coord(0, self.height - SCALE)
            self.p2 = Coord(self.width - self.height+2*SCALE, self.height - SCALE)
            self.p3 = Coord(self.width, SCALE)
            text_y_default = self.height-4
        elif self.ori == 'sw':
            self.p1 = Coord(0, self.height - SCALE)
            self.p2 = Coord(self.height-2*SCALE, SCALE)
            self.p3 = Coord(self.width, SCALE)
            text_y_default = 4
        elif self.ori == 'se':
            self.p1 = Coord(0, SCALE)
            self.p2 = Coord(self.width - self.height+2*SCALE, SCALE)
            self.p3 = Coord(self.width, self.height - SCALE)
            text_y_default = 4
        else:
            self.p1 = Coord(0, SCALE)
            self.p2 = Coord(self.width - self.height+2*SCALE, SCALE)
            self.p3 = Coord(self.width, self.height - SCALE)
            text_y_default = 4

        self.text_x = self.placement.get('text_x', self.width / 2)
        self.text_y = self.placement.get('text_y', text_y_default)
        self.text_anchor = self.placement.get('text_anchor', 'center')

        self.line = self.canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, self.p3.x, self.p3.y,  width=4, capstyle='butt', smooth=False)
        self.canvas.itemconfig(self.line, fill='yellow')
        self.canvas.create_text(self.text_x, self.text_y, text=self.name, font=('Helvetica', 6), anchor=self.text_anchor)
        self.section_separatorA = self.canvas.create_line(self.p1.x, self.p1.y-4, self.p1.x, self.p1.y+4)
        self.section_separatorB = self.canvas.create_line(self.p3.x, self.p3.y-4, self.p3.x, self.p3.y+4)


    def place_widget(self, display_objects):
        self.canvas.pack()
        if 'in_' in self.placement:
            # placement relative to another display_object using _in, anchor, relx, rely
            self.place(in_=display_objects[self.placement['in_']],
                             **{k: v for k, v in self.placement.items() if k in ('anchor', 'relx', 'rely')})
        else:
            # placement using master frame coordinates
            self.place(**{k: v for k, v in self.placement.items() if k in ('x', 'y')})


def TrackSectionWidget_constructor(loader: yaml.SafeLoader, node: yaml.nodes.MappingNode) -> TrackSectionWidget:
    return TrackSectionWidget(**loader.construct_mapping(node))
