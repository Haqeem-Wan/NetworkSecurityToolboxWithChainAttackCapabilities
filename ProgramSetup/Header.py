from tkinter import *
from ProgramSetup.NavMenu import *

class Header:
    def __init__ (self, root, headerFrame, contentFrame):
        self.root = root
        self.headerFrame = headerFrame
        self.contentFrame = contentFrame

        self.navMenuFrame = Frame(self.root, bg="#333333", height=720, width=300)
        self.navMenuFrame.place(x=-300, y=0)
        Label(self.navMenuFrame, font="Bahnschrift 15", bg="#333333", fg="#454545", height=2, width=300, padx=20).place(x=0, y=0)

        self.navMenuContents = NavMenu(self.root, self.headerFrame, self.navMenuFrame, self.contentFrame)

    def leftclick(self, event):
        NavMenu.toggleNavMenu()
    