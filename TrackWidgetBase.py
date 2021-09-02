import tkinter as tk

SCALE = 10


class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y


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

    def place_widget(self, display_widgets):
        self.canvas.pack()
        if 'in_' in self.placement:
            # placement relative to another display_object using _in, anchor, relx, rely
            self.place(in_=display_widgets[self.placement['in_']],
                             **{k: v for k, v in self.placement.items() if k in ('anchor', 'relx', 'rely')})
        else:
            # placement using master frame coordinates
            self.place(**{k: v for k, v in self.placement.items() if k in ('x', 'y')})

    def mouse_enter(self, event):
        print(f'Entered: {self.name}')

    def mouse_leave(self, event):
        print(f'Left: {self.name}')
