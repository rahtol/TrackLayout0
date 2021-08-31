import tkinter as tk
from PointWidget import *


class FarstaStrandGui:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master, height=400, width=3200)
        self.frame.pack()
        master.title("Farsta Strand Gui")

        self.pt_1011 = PointWidget(self.frame, '1011', ori=ORI_NE, h=4, w=3)
        self.pt_1011.place(x=150, y=20)
        self.pt_1012 = PointWidget(self.frame, '1012', ori=ORI_NW, h=4, w=3)
        self.pt_1012.place(x=120, y=20)
        self.pt_A1012 = PointWidget(self.frame, 'A1012', ori=ORI_SE, h=4, w=4)
        self.pt_A1012.place(x=80, y=0)
        self.pt_A1011 = PointWidget(self.frame, 'A1012', ori=ORI_SW, h=4, w=4)
        self.pt_A1011.place(x=180, y=0)

#        self.frame.pack(expand=1)


root = tk.Tk()
gui = FarstaStrandGui(root)
root.mainloop()
