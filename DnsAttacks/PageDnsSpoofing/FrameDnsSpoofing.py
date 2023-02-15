from tkinter import *

class FrameDnsSpoofing:
    def __init__ (self, frame):
        self.attackFrame = frame

        self.testLabel = Label(self.attackFrame, text="DNS Spoofing", fg="#ffffff", font="bahnschrift 15")
        self.testLabel.pack()