from tkinter import *
from tkinter.ttk import Separator
from Layer2Attacks.PageCamAttacks.funcFrameCam import *

class FrameCam:
    def __init__ (self, frame):
        self.attackFrame = frame

        self.targetIpLabel = Label(self.attackFrame, text="Target IP Address                    :", fg="#ffffff", bg="#0078bd", font="bahnschrift 15")
        self.targetIpLabel.place(x = 85, y = 45)

        self.targetIpEntry = Entry(self.attackFrame, width = 40, font="bahnschrift 15", fg="#ffffff", bg="#252525")
        self.targetIpEntry.place(x = 435, y = 45)

        self.packetNumberLabel = Label(self.attackFrame, text="Number of Packets to send     :", fg="#ffffff", bg="#0078bd", font="bahnschrift 15")
        self.packetNumberLabel.place(x = 85, y = 95)

        self.packetNumberEntry = Entry(self.attackFrame, width = 40, font="bahnschrift 15", fg="#ffffff", bg="#252525")
        self.packetNumberEntry.place(x = 435, y = 95)


        self.separator = Separator(self.attackFrame, orient="horizontal")
        self.separator.pack(fill = X, expand = TRUE, pady = 175)

        self.terminalLabel = Label(self.attackFrame, text="Terminal", fg="#ffffff", bg="#0078bd", font="bahnschrift 15")
        self.terminalLabel.place(x = 285, y = 180)

        self.wiresharkLabel = Label(self.attackFrame, text="Wireshark", fg="#ffffff", bg="#0078bd", font="bahnschrift 15")
        self.wiresharkLabel.place(x = 890, y = 180)

        self.errorNotesLabel = Label(self.attackFrame, text="Errors and Notes", fg="#ffffff", bg="#0078bd", font="bahnschrift 15")
        self.errorNotesLabel.place(x = 550, y = 480)



        self.terminalFrame = Frame(self.attackFrame, width=500, height=260, background="#252525", highlightbackground="#ffffff", highlightthickness=2)
        self.terminalFrame.pack_propagate(False)
        self.terminalFrame.place(x = 90, y = 210)

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



        self.wiresharkFrame = Frame(self.attackFrame, width=500, height=260, background="#252525", highlightbackground="#ffffff", highlightthickness=2)
        self.wiresharkFrame.pack_propagate(False)
        self.wiresharkFrame.place(x = 690, y = 210)

        self.wiresharkScrollCanvas = Canvas(self.wiresharkFrame, background="#252525", highlightbackground="#ffffff", yscrollincrement=8)
        self.wiresharkScrollCanvas.pack(side = LEFT, fill = BOTH, expand = 1)
       
        self.wiresharkScrollbar = Scrollbar(self.wiresharkFrame, orient=VERTICAL, command = self.wiresharkScrollCanvas.yview)
        self.wiresharkScrollbar.pack(side = RIGHT, fill = Y)

        self.wiresharkScrollCanvas.configure(yscrollcommand=self.wiresharkScrollbar.set)
        self.wiresharkScrollCanvas.bind("<Configure>", lambda e : self.wiresharkScrollCanvas.configure(scrollregion=self.wiresharkScrollCanvas.bbox("all")))
        self.wiresharkFrame.bind_all("<MouseWheel>", lambda e : self.wiresharkScrollCanvas.yview_scroll(-1, "units"))

        self.wiresharkContentFrame = Frame(self.wiresharkScrollCanvas, background="#252525", highlightbackground="#ffffff")
        self.wiresharkScrollCanvas.create_window((0,0), window = self.wiresharkContentFrame, anchor = NW)
        self.wiresharkContentFrame.bind("<Configure>", lambda e : self.wiresharkScrollCanvas.configure(scrollregion=self.wiresharkScrollCanvas.bbox("all")))



        self.errorOutputFrame = Frame(self.attackFrame, width=500, height=100, background="#252525", highlightbackground="#ffffff", highlightthickness=2)
        self.errorOutputFrame.pack_propagate(False)
        self.errorOutputFrame.place(x = 390, y = 515)

        self.errorOutputScrollCanvas = Canvas(self.errorOutputFrame, background="#252525", highlightbackground="#ffffff", yscrollincrement=8)
        self.errorOutputScrollCanvas.pack(side = LEFT, fill = BOTH, expand = 1)
       
        self.errorOutputScrollbar = Scrollbar(self.errorOutputFrame, orient=VERTICAL, command = self.errorOutputScrollCanvas.yview)
        self.errorOutputScrollbar.pack(side = RIGHT, fill = Y)

        self.errorOutputScrollCanvas.configure(yscrollcommand=self.errorOutputScrollbar.set)
        self.errorOutputScrollCanvas.bind("<Configure>", lambda e : self.errorOutputScrollCanvas.configure(scrollregion=self.errorOutputScrollCanvas.bbox("all")))
        self.errorOutputFrame.bind_all("<MouseWheel>", lambda e : self.errorOutputScrollCanvas.yview_scroll(-1, "units"))

        self.errorOutputContentFrame = Frame(self.errorOutputScrollCanvas, background="#252525", highlightbackground="#ffffff")
        self.errorOutputScrollCanvas.create_window((0,0), window = self.errorOutputContentFrame, anchor = NW)
        self.errorOutputContentFrame.bind("<Configure>", lambda e : self.errorOutputScrollCanvas.configure(scrollregion=self.errorOutputScrollCanvas.bbox("all")))




        self.startButton = Button(self.attackFrame, height=3, width=10, font="bahnschrift 15", text="Start", fg="#ffffff", bg="#252525", 
                                  command=lambda : startCam(self.targetIpEntry.get(), self.packetNumberEntry.get(), self.terminalContentFrame, self.errorOutputContentFrame))
        self.startButton.place(x = 1010, y = 43)