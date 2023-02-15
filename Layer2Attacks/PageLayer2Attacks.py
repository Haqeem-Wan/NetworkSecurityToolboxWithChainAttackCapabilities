from tkinter import *
from Layer2Attacks.PageArpAttacks.FrameArp import *
from Layer2Attacks.PageCamAttacks.FrameCam import *
from Layer2Attacks.PageDhcpAttacks.FrameDhcp import *
from Layer2Attacks.PageMacAttacks.FrameMac import *
from Layer2Attacks.PageStpAttacks.FrameStp import *
from Layer2Attacks.PageVlanAttacks.FrameVlan import *

class PageLayer2Attacks:
    def __init__ (self, frame):
        self.layer2Frame = frame
        self.navLayer2Frame = Frame(self.layer2Frame, width=1280, height=40, background="#454545")
        self.attackFrame = Frame(self.layer2Frame, width=1280, height=580, background="#454545")

        self.navLayer2Options = ["CAM Table Overflow", "VLAN Hopping", "DHCP Attack", "ARP Poisoning Attack", "MAC Address Spoofing", "STP Attack"]
        self.navLayer2Links = [self.showFrameCam, self.showFrameVlan, self.showFrameDhcp, self.showFrameArp, self.showFrameMac, self.showFrameStp]
        for i in range(len(self.navLayer2Options)):
            button = Button(self.navLayer2Frame, text=self.navLayer2Options[i], height=100, width = 19, font="BahnschriftLight 12", bg="#333333", fg="#ffffff", 
            activebackground="#333333", activeforeground="#9e9e9e", highlightthickness=0, bd=0, borderwidth=3,relief="raised", 
            command=self.navLayer2Links[i])
            button.pack(side=LEFT)
        
        self.navLayer2Frame.pack_propagate(0)
        self.navLayer2Frame.pack()
        self.attackFrame.pack_propagate(0)
        self.attackFrame.pack()

    def showFrameCam(self):
        self.deletePages()
        self.camFrame = Frame(self.attackFrame, width=1280, height=580, background="#454545")
        self.camContents = FrameCam(self.attackFrame)
        self.camFrame.pack()
    
    def showFrameVlan(self) :
        self.deletePages()
        self.vlanFrame = Frame(self.attackFrame, width=1280, height=580, background="#454545")
        self.vlanContents = FrameVlan(self.attackFrame)
        self.vlanFrame.pack()

    def showFrameArp(self) :
        self.deletePages()
        self.arpFrame = Frame(self.attackFrame, width=1280, height=580, background="#454545")
        self.arpContents = FrameArp(self.attackFrame)
        self.arpFrame.pack()
    
    def showFrameDhcp(self):
        self.deletePages()
        self.dhcpFrame = Frame(self.attackFrame, width=1280, height=580, background="#454545")
        self.dhcpContents = FrameDhcp(self.attackFrame)
        self.dhcpFrame.pack()

    def showFrameMac(self) :
        self.deletePages()
        self.macFrame = Frame(self.attackFrame, width=1280, height=580, background="#454545")
        self.macContents = FrameMac(self.attackFrame)
        self.macFrame.pack()
    
    def showFrameStp(self) :
        self.deletePages()
        self.stpFrame = Frame(self.attackFrame, width=1280, height=580, background="#454545")
        self.stpContents = FrameStp(self.attackFrame)
        self.stpFrame.pack()

    def deletePages(self):
        for frame in self.attackFrame.winfo_children():
            frame.destroy()