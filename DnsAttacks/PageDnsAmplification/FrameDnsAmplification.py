from tkinter import *

class FrameDnsAmplification:
    def __init__ (self, frame):
        self.attackFrame = frame

        self.testLabel = Label(self.attackFrame, text="DNS Amplification", fg="#ffffff", font="bahnschrift 15")
        self.testLabel.pack()