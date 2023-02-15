from tkinter import *

class FrameDhcp:
    def __init__ (self, frame):
        self.attackFrame = frame

        self.testLabel = Label(self.attackFrame, text="Dhcp", fg="#ffffff", font="bahnschrift 15")
        self.testLabel.pack()