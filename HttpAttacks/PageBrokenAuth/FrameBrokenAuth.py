from tkinter import *

class FrameBrokenAuth:
    def __init__ (self, frame):
        self.attackFrame = frame

        self.testLabel = Label(self.attackFrame, text="Broken Auth.", fg="#ffffff", font="bahnschrift 15")
        self.testLabel.pack()