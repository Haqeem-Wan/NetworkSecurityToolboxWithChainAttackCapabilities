from tkinter import *

class FrameDnsHijacking:
    def __init__ (self, frame):
        self.attackFrame = frame

        self.testLabel = Label(self.attackFrame, text="DNS Hijacking", fg="#ffffff", font="bahnschrift 15")
        self.testLabel.pack()