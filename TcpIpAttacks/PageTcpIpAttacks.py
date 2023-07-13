from tkinter import *
from TcpIpAttacks.PageIcmpAttacks.FrameIcmpAttacks import *
from TcpIpAttacks.PageSynFlooding.FrameSynFlooding import *

class PageTcpIpAttacks:
    def __init__ (self, frame):
        self.tcpIpFrame = frame
        self.navTcpIpFrame = Frame(self.tcpIpFrame, width=1280, height=40, background="#295543")
        self.attackFrame = Frame(self.tcpIpFrame, width=1280, height=630, background="#295543")

        self.synFloodButton = Button(self.navTcpIpFrame, height=100, width = 63, font="BahnschriftLight 12", bg="#2E6E53", fg="#ffffff", 
                                     activebackground="#295543", activeforeground="#1A3329", highlightthickness=0, bd=0, borderwidth=3,relief="raised")
        self.icmpButton = Button(self.navTcpIpFrame, height=100, width = 63, font="BahnschriftLight 12", bg="#2E6E53", fg="#ffffff", 
                                 activebackground="#295543", activeforeground="#1A3329", highlightthickness=0, bd=0, borderwidth=3,relief="raised")
        
        self.navTcpIpOptions = ["Syn Flooding", "ICMP Attacks"]
        self.navTcpIpLinks = [self.showFrameSynFlooding, self.showFrameIcmpAttacks]
        self.navTcpIpButtons = [self. synFloodButton, self.icmpButton]
        
        for i in range(len(self.navTcpIpOptions)):
            self.navTcpIpButtons[i].config(text=self.navTcpIpOptions[i])
            self.navTcpIpButtons[i].config(command=self.navTcpIpLinks[i])
            self.navTcpIpButtons[i].pack(side=LEFT)

        self.navTcpIpFrame.pack_propagate(0)
        self.navTcpIpFrame.pack()
        self.attackFrame.pack_propagate(0)
        self.attackFrame.pack()

        self.showFrameSynFlooding()

    def showFrameSynFlooding(self):
        self.deletePages()
        self.synFloodingFrame = Frame(self.attackFrame, width=1280, height=580, background="#295543")
        self.synFloodingContents = FrameSynFlooding(self.attackFrame)
        self.synFloodingFrame.pack()

        self.configureButtons("Syn Flooding")
    
    def showFrameIcmpAttacks(self) :
        self.deletePages()
        self.icmpAttacksFrame = Frame(self.attackFrame, width=1280, height=580, background="#295543")
        self.icmpAttacksContents = FrameIcmpAttacks(self.attackFrame)
        self.icmpAttacksFrame.pack()

        self.configureButtons("ICMP Attacks")

    def configureButtons(self, buttonPressed) :
        for i in range(len(self.navTcpIpOptions)):
            if self.navTcpIpOptions[i] == buttonPressed :
                self.navTcpIpButtons[i].config(relief="sunken")
                self.navTcpIpButtons[i].config(state="disabled")
            else :
                self.navTcpIpButtons[i].config(relief="raised")
                self.navTcpIpButtons[i].config(state="normal")

    def deletePages(self):
        for frame in self.attackFrame.winfo_children():
            frame.destroy()