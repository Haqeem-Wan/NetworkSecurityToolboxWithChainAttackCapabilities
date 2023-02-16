from tkinter import *
from TcpIpAttacks.PageIcmpAttacks.FrameIcmpAttacks import *
from TcpIpAttacks.PageIpSpoofing.FrameIpSoofing import *
from TcpIpAttacks.PageSeqNumAttacks.FrameSeqNumAttacks import *
from TcpIpAttacks.PageSslStrip.FrameSslStrip import *
from TcpIpAttacks.PageSynFlooding.FrameSynFlooding import *
from TcpIpAttacks.PageTcpSessionHijacking.FrameTcpSessionHijacking import *

class PageTcpIpAttacks:
    def __init__ (self, frame):
        self.tcpIpFrame = frame
        self.navTcpIpFrame = Frame(self.tcpIpFrame, width=1280, height=40, background="#295543")
        self.attackFrame = Frame(self.tcpIpFrame, width=1280, height=580, background="#295543")

        self.navTcpIpOptions = ["Syn Flooding", "ICMP Attacks", "SeqNum Predic. Attacks", "TCP Session Hijacking", "IP Spoofing", "SSL Strip"]
        self.navTcpIpLinks = [self.showFrameSynFlooding, self.showFrameIcmpAttacks, self.showFrameSeqNumAttacks, 
        self.showFrameTcpSessionHijacking, self.showFrameIpSpoofing, self.showFrameSslStrip]
        for i in range(len(self.navTcpIpOptions)):
            button = Button(self.navTcpIpFrame, text=self.navTcpIpOptions[i], height=100, width = 19, font="BahnschriftLight 12", bg="#2E6E53", fg="#ffffff", 
            activebackground="#295543", activeforeground="#1A3329", highlightthickness=0, bd=0, borderwidth=3,relief="raised", 
            command=self.navTcpIpLinks[i])
            button.pack(side=LEFT)

        self.navTcpIpFrame.pack_propagate(0)
        self.navTcpIpFrame.pack()
        self.attackFrame.pack_propagate(0)
        self.attackFrame.pack()

    def showFrameSynFlooding(self):
        self.deletePages()
        self.synFloodingFrame = Frame(self.attackFrame, width=1280, height=580, background="#295543")
        self.synFloodingContents = FrameSynFlooding(self.attackFrame)
        self.synFloodingFrame.pack()
    
    def showFrameIcmpAttacks(self) :
        self.deletePages()
        self.icmpAttacksFrame = Frame(self.attackFrame, width=1280, height=580, background="#295543")
        self.icmpAttacksContents = FrameIcmpAttacks(self.attackFrame)
        self.icmpAttacksFrame.pack()

    def showFrameSeqNumAttacks(self) :
        self.deletePages()
        self.seqNumAttacksFrame = Frame(self.attackFrame, width=1280, height=580, background="#295543")
        self.seqNumAttacksContents = FrameSeqNumAttacks(self.attackFrame)
        self.seqNumAttacksFrame.pack()
    
    def showFrameTcpSessionHijacking(self):
        self.deletePages()
        self.tcpSessionHijackingFrame = Frame(self.attackFrame, width=1280, height=580, background="#295543")
        self.tcpSessionHijackingContents = FrameTcpSessionHijacking(self.attackFrame)
        self.tcpSessionHijackingFrame.pack()

    def showFrameIpSpoofing(self) :
        self.deletePages()
        self.ipSpoofingFrame = Frame(self.attackFrame, width=1280, height=580, background="#295543")
        self.ipSpoofingContents = FrameIpSpoofing(self.attackFrame)
        self.ipSpoofingFrame.pack()
    
    def showFrameSslStrip(self) :
        self.deletePages()
        self.sslStripFrame = Frame(self.attackFrame, width=1280, height=580, background="#295543")
        self.sslStripContents = FrameSslStrip(self.attackFrame)
        self.sslStripFrame.pack()

    def deletePages(self):
        for frame in self.attackFrame.winfo_children():
            frame.destroy()