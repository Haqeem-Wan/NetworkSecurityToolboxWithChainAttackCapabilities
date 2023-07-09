from tkinter import *
from tkinter.ttk import Separator

class PageChainAttacks :
    def __init__ (self, frame) :
        self.chainAttacksFrame = frame
        self.attackDirectoryFrame = Frame(self.chainAttacksFrame, width=1280, height=80, background="#bf4900")

        self.attackDirectoryFrame.pack_propagate(0)
        self.attackDirectoryFrame.pack()