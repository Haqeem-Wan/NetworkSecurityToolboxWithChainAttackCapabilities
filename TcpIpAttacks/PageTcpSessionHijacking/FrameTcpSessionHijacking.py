from tkinter import *

class FrameTcpSessionHijacking:
    def __init__ (self, frame):
        self.attackFrame = frame

        self.testLabel = Label(self.attackFrame, text="TCP Session Hijacking", fg="#ffffff", font="bahnschrift 15")
        self.testLabel.pack()