from tkinter import *

class FrameMac:
    def __init__ (self, frame):
        self.attackFrame = frame

        self.testLabel = Label(self.attackFrame, text="Mac", fg="#ffffff", font="bahnschrift 15")
        self.testLabel.pack()