from tkinter import *

class FrameIpSpoofing:
    def __init__ (self, frame):
        self.attackFrame = frame

        self.testLabel = Label(self.attackFrame, text="IP Spoofing", fg="#ffffff", font="bahnschrift 15")
        self.testLabel.pack()