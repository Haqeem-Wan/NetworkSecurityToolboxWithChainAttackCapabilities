from tkinter import *

class PageHome:
    def __init__ (self, frame):
        self.homeFrame = frame

        self.testLabel = Label(self.homeFrame, text="Home", fg="#ffffff", bg="#454545", font="bahnschrift 15")
        self.testLabel.pack()