from tkinter import *

class FrameSslStrip:
    def __init__ (self, frame):
        self.attackFrame = frame

        self.testLabel = Label(self.attackFrame, text="SSL Strip", fg="#ffffff", font="bahnschrift 15")
        self.testLabel.pack()