from tkinter import *

class FrameDos:
    def __init__ (self, frame):
        self.attackFrame = frame

        self.testLabel = Label(self.attackFrame, text="DOS", fg="#ffffff", font="bahnschrift 15")
        self.testLabel.pack()