from tkinter import *

class FrameSensitiveDataExpo:
    def __init__ (self, frame):
        self.attackFrame = frame

        self.testLabel = Label(self.attackFrame, text="Sensitive Data Expo", fg="#ffffff", font="bahnschrift 15")
        self.testLabel.pack()