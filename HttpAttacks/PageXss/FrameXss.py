from tkinter import *

class FrameXss:
    def __init__ (self, frame):
        self.attackFrame = frame

        self.testLabel = Label(self.attackFrame, text="XSS", fg="#ffffff", font="bahnschrift 15")
        self.testLabel.pack()