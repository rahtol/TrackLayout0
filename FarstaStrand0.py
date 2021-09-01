import tkinter as tk
from PointWidget import *


class FarstaStrandGui:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master, height=400, width=1600)
        self.frame.pack()
        master.title("Farsta Strand Gui")

        self.pt_1011 = PointWidget(self.frame, '1011', ori=ORI_NE, height=5, width=4)
        self.pt_1011.place(x=150, y=30)
        self.pt_1012 = PointWidget(self.frame, '1012', ori=ORI_NW, height=5, width=4)
#        self.pt_1012.place(x=110, y=30)
        self.pt_A1012 = PointWidget(self.frame, 'A1012', ori=ORI_SE, height=5, width=5)
        self.pt_A1012.place(x=60, y=0)
        self.pt_A1011 = PointWidget(self.frame, 'A1011', ori=ORI_SW, height=5, width=5)
        self.pt_A1011.place(x=190, y=0)

        self.pt_1012.place(in_=self.pt_A1012, anchor='nw', relx=1.0, rely=0.6)

#        self.frame.pack(expand=1)


root = tk.Tk()
gui = FarstaStrandGui(root)
root.mainloop()
