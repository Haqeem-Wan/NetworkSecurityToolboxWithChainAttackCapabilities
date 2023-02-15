from tkinter import *
from tkinter.ttk import Separator
from Layer2Attacks.PageArpAttacks.funcFrameArp import *

class FrameArp:
    def __init__ (self, frame):
        self.attackFrame = frame

        self.targetIpLabel = Label(self.attackFrame, text="Target IP Address             :", fg="#ffffff", bg="#454545", font="bahnschrift 15")
        self.targetIpLabel.place(x = 85, y = 20)

        self.targetDefaultGateLabel = Label(self.attackFrame,   text="Target Default Gateway   :", fg="#ffffff", bg="#454545", font="bahnschrift 15")
        self.targetDefaultGateLabel.place(x = 85, y = 70)

        self.targetIpEntry = Entry(self.attackFrame, width = 40, font="bahnschrift 15", fg="#ffffff", bg="#252525")
        self.targetIpEntry.place(x = 435, y = 20)

        self.targetDefaultGateEntry = Entry(self.attackFrame, width = 40, font="bahnschrift 15", fg="#ffffff", bg="#252525")
        self.targetDefaultGateEntry.place(x = 435, y = 70)

        self.startButton = Button(self.attackFrame, height=3, width=5, font="bahnschrift 15", text="Start", fg="#ffffff", bg="#252525", command=testFunc)
        self.startButton.place(x = 1010, y = 18)

        self.stopButton = Button(self.attackFrame, height=3, width=5, font="bahnschrift 15", text="Stop", fg="#ffffff", bg="#252525", command=testFuncAgain)
        self.stopButton.place(x = 1102, y = 18)

        self.separator = Separator(self.attackFrame, orient="horizontal")
        self.separator.pack(fill = X, expand = TRUE, pady = 125)

        self.terminalLabel = Label(self.attackFrame, text="Terminal", fg="#ffffff", bg="#454545", font="bahnschrift 15")
        self.terminalLabel.place(x = 285, y = 130)

        self.wiresharkLabel = Label(self.attackFrame, text="Wireshark", fg="#ffffff", bg="#454545", font="bahnschrift 15")
        self.wiresharkLabel.place(x = 890, y = 130)

        self.errorNotesLabel = Label(self.attackFrame, text="Errors and Notes", fg="#ffffff", bg="#454545", font="bahnschrift 15")
        self.errorNotesLabel.place(x = 550, y = 430)

        self.terminalFrame = Frame(self.attackFrame, width=500, height=260, background="#252525", highlightbackground="#ffffff", highlightthickness=2)
        self.terminalFrame.place(x = 90, y = 160)

        self.wiresharkFrame = Frame(self.attackFrame, width=500, height=260, background="#252525", highlightbackground="#ffffff", highlightthickness=2)
        self.wiresharkFrame.place(x = 690, y = 160)
        
        self.errorOutputFrame = Frame(self.attackFrame, width=500, height=100, background="#252525", highlightbackground="#ffffff", highlightthickness=2)
        self.errorOutputFrame.place(x = 390, y = 465)