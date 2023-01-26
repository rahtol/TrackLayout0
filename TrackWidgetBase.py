import tkinter as tk

SCALE = 10


class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def default_placement(anchor : str):
    if anchor == 'nw':
        return (1.0, 0.0)
    elif anchor == 'sw':
        return (1.0, 1.0)
    elif anchor == 'ne':
        return (0.0, 0.0)
    elif anchor == 'se':
        return (0.0, 1.0)
    else:
        return(0.5, 0.5)


class TrackWidgetBase(tk.Frame):
    def __init__(self, *, ori, height, width, **placement):
        self.ori = ori
        self.height = height
        self.width = width
        self.placement = placement
        self.name = '???'
        self.gui = None
        self.master_frame = None
        self.canvas = None

    def create_widget(self, name, master_frame, gui):
        self.name = name
        self.master_frame = master_frame
        self.gui = gui
        tk.Frame.__init__(self, self.master_frame, height=self.height, width=self.width)
        self.canvas = tk.Canvas(self, height=self.height, width=self.width, highlightthickness=0, bg='gray85')
        self.bind('<Any-Enter>', self.mouse_enter)
        self.bind('<Any-Leave>', self.mouse_leave)

    def place_widget(self, display_widgets):
        self.canvas.pack()
        if 'in_' in self.placement:
            # placement relative to another display_object using _in, anchor, relx or x, rely or y
            # 'anchor' specifies a coordinate of self widget, i.e. one of its corners using nw, sw, ne or se
            # (x, y) or (relx, rely) specify a coordinate of the reference widget _in
            # the self widget will be placed so that both coordinates align
            if {'x', 'y', 'relx', 'rely'}.isdisjoint(self.placement.keys()):
                # if none of the above keys is present provide defaults based on value of 'anchor'
                (self.placement['relx'], self.placement['rely']) = default_placement(self.placement['anchor'])
            in_ = display_widgets[self.placement['in_']]
            symbols = {'nw': 'nw', 'ne': 'ne', 'sw': 'sw', 'se': 'se', 'in_': in_}
            self.place(in_=in_, **{k: eval(str(v), globals(), symbols)
                                   for k, v in self.placement.items() if k in ('anchor', 'relx', 'rely', 'x', 'y')})
        else:
            # placement using master frame coordinates
            self.place(**{k: v for k, v in self.placement.items() if k in ('x', 'y')})

    def mouse_enter(self, event):
        print(f'Entered: {self.name}')

    def mouse_leave(self, event):
        print(f'Left: {self.name}')
