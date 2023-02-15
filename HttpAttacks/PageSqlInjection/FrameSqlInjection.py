from tkinter import *

class FrameSqlInjection:
    def __init__ (self, frame):
        self.attackFrame = frame

        self.testLabel = Label(self.attackFrame, text="Sql Injection", fg="#ffffff", font="bahnschrift 15")
        self.testLabel.pack()