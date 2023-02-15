from tkinter import *

class FrameSynFlooding:
    def __init__ (self, frame):
        self.attackFrame = frame

        self.testLabel = Label(self.attackFrame, text="Syn Flooding", fg="#ffffff", font="bahnschrift 15")
        self.testLabel.pack()