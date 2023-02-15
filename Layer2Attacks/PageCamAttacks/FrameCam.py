from tkinter import *

class FrameCam:
    def __init__ (self, frame):
        self.attackFrame = frame
        self.puttyFrame = Frame(self.attackFrame, width=500, height=300, background="#08CA22")
        self.terminalFrame = Frame()

        self.puttyFrame.place(x = 50, y = 50)