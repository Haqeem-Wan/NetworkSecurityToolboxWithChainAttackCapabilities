from tkinter import *

class FrameStp:
    def __init__ (self, frame):
        self.attackFrame = frame

        self.testLabel = Label(self.attackFrame, text="Stp", fg="#ffffff", font="bahnschrift 15")
        self.testLabel.pack()