import tkinter as tk
import yaml

from PointWidget import PointWidget_constructor
from TrackSectionWidget import TrackSectionWidget_constructor


def get_loader():
    """Add constructors to PyYAML loader."""
    loader = yaml.SafeLoader
    loader.add_constructor("!TrackSectionWidget", TrackSectionWidget_constructor)
    loader.add_constructor("!PointWidget", PointWidget_constructor)
    return loader


class FarstaStrandGui:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master, height=400, width=1600)
        self.frame.pack()
        master.title("Farsta Strand Gui #2")

        stream = open("FarstaStrandLayout.yaml", 'r')
        self.yaml = yaml.load(stream, Loader=get_loader())
        display_widgets = self.yaml['display_elements']

        for name, widget in display_widgets.items():
            widget.create_widget(name, self.frame)
        for widget in display_widgets.values():
            widget.place_widget(display_widgets)


root = tk.Tk()
gui = FarstaStrandGui(root)
root.mainloop()
