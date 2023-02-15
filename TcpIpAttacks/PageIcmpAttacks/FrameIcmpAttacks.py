from tkinter import *

class FrameIcmpAttacks:
    def __init__ (self, frame):
        self.attackFrame = frame

        self.testLabel = Label(self.attackFrame, text="ICMP Attacks", fg="#ffffff", font="bahnschrift 15")
        self.testLabel.pack()