import tkinter as tk
import yaml

from PointWidget import PointWidget_constructor
from TrackSectionWidget import TrackSectionWidget_constructor
from SignalWidget import SignalWidget_constructor


def get_loader():
    """Add constructors to PyYAML loader."""
    loader = yaml.SafeLoader
    loader.add_constructor("!TrackSectionWidget", TrackSectionWidget_constructor)
    loader.add_constructor("!PointWidget", PointWidget_constructor)
    loader.add_constructor("!SignalWidget", SignalWidget_constructor)
    return loader


class FarstaStrandGui:
    def __init__(self, master):
        self.master = master
        self.frame0 = tk.Frame(self.master)

        self.canvas = tk.Canvas(self.frame0, height=400, width=1900, highlightthickness=0)
        self.frame = tk.Frame(self.canvas, height=400, width=3800, bg='gray85')
        self.hsb = tk.Scrollbar(self.frame0, orient="horizontal", command=self.canvas.xview)
        self.canvas.configure(xscrollcommand=self.hsb.set)
        self.hsb.pack(side="bottom", fill="x")
        self.canvas.pack(side="top", fill="both", expand=True)
        self.canvas.create_window((0,0), window=self.frame, anchor="nw", tags="self.frame")
        self.frame.bind("<Configure>", self.onFrameConfigure)
        self.frame0.pack()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        self.canvas.xview_moveto(1.0)

        master.title("Farsta Strand Gui #2")

        stream = open("FarstaStrandLayout.yaml", 'r')
        self.yaml = yaml.load(stream, Loader=get_loader())
        display_widgets = self.yaml['display_elements']

        for name, widget in display_widgets.items():
            widget.create_widget(name, self.frame, self)
        for widget in display_widgets.values():
            widget.place_widget(display_widgets)

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

root = tk.Tk()
gui = FarstaStrandGui(root)
root.mainloop()
