from tkinter import *

class FrameDnsTunneling:
    def __init__ (self, frame):
        self.attackFrame = frame

        self.testLabel = Label(self.attackFrame, text="DNS Tunneling", fg="#ffffff", font="bahnschrift 15")
        self.testLabel.pack()