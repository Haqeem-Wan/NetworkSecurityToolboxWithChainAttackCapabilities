from tkinter import *
from tkinter.ttk import Separator
from Layer2Attacks.PageCamAttacks.funcFrameCam import *

class FrameCam:
    def __init__ (self, frame):
        self.attackFrame = frame

        self.targetIpLabel = Label(self.attackFrame, text="Target IP Address             :", fg="#ffffff", bg="#454545", font="bahnschrift 15")
        self.targetIpLabel.place(x = 85, y = 20)

        self.targetIpEntry = Entry(self.attackFrame, width = 40, font="bahnschrift 15", fg="#ffffff", bg="#252525")
        self.targetIpEntry.place(x = 435, y = 20)

        self.portFrame = Frame(self.attackFrame, width=500, height=300, background="#08CA22")
        self.terminalFrame = Frame()

        self.separator = Separator(self.attackFrame, orient="horizontal")
        self.separator.pack(fill = X, expand = TRUE, pady = 125)

        self.terminalLabel = Label(self.attackFrame, text="Terminal", fg="#ffffff", bg="#454545", font="bahnschrift 15")
        self.terminalLabel.place(x = 285, y = 130)

        self.wiresharkLabel = Label(self.attackFrame, text="Wireshark", fg="#ffffff", bg="#454545", font="bahnschrift 15")
        self.wiresharkLabel.place(x = 890, y = 130)

        self.errorNotesLabel = Label(self.attackFrame, text="Errors and Notes", fg="#ffffff", bg="#454545", font="bahnschrift 15")
        self.errorNotesLabel.place(x = 550, y = 430)

        self.terminalFrame = Frame(self.attackFrame, width=500, height=260, background="#252525", highlightbackground="#ffffff", highlightthickness=2)
        self.terminalFrame.pack_propagate(False)
        self.terminalFrame.place(x = 90, y = 160)

        self.terminalScrollCanvas = Canvas(self.terminalFrame, background="#252525", highlightbackground="#ffffff", yscrollincrement=8)
        self.terminalScrollCanvas.pack(side = LEFT, fill = BOTH, expand = 1)
       
        self.terminalScrollbar = Scrollbar(self.terminalFrame, orient=VERTICAL, command = self.terminalScrollCanvas.yview)
        self.terminalScrollbar.pack(side = RIGHT, fill = Y)

        self.terminalScrollCanvas.configure(yscrollcommand=self.terminalScrollbar.set)
        self.terminalScrollCanvas.bind("<Configure>", lambda e : self.terminalScrollCanvas.configure(scrollregion=self.terminalScrollCanvas.bbox("all")))
        self.terminalScrollCanvas.bind_all("<MouseWheel>", lambda e : self.terminalScrollCanvas.yview_scroll(-1, "units"))

        self.terminalContentFrame = Frame(self.terminalScrollCanvas, background="#252525", highlightbackground="#ffffff")
        self.terminalScrollCanvas.create_window((0,0), window = self.terminalContentFrame, anchor = NW)
        self.terminalContentFrame.bind("<Configure>", lambda e : self.terminalScrollCanvas.configure(scrollregion=self.terminalScrollCanvas.bbox("all")))

        self.portFrame.place(x = 50, y = 50)
