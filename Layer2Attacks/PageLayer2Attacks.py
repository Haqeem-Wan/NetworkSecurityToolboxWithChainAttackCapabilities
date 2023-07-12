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
        self.navLayer2Frame = Frame(self.layer2Frame, width=1280, height=40, background="#0078bd")
        self.attackFrame = Frame(self.layer2Frame, width=1280, height=630, background="#0078bd")

        self.camButton = Button(self.navLayer2Frame, height=100, width = 19, font="BahnschriftLight 12", bg="#0973de", fg="#ffffff", 
                                activebackground="#0973de", activeforeground="#9e9e9e", highlightthickness=0, bd=0, borderwidth=3,relief="raised")
        self.vlanButton = Button(self.navLayer2Frame, height=100, width = 19, font="BahnschriftLight 12", bg="#0973de", fg="#ffffff", 
                                activebackground="#0973de", activeforeground="#9e9e9e", highlightthickness=0, bd=0, borderwidth=3,relief="raised")
        self.arpButton = Button(self.navLayer2Frame, height=100, width = 19, font="BahnschriftLight 12", bg="#0973de", fg="#ffffff", 
                                activebackground="#0973de", activeforeground="#9e9e9e", highlightthickness=0, bd=0, borderwidth=3,relief="raised")
        self.dhcpButton = Button(self.navLayer2Frame, height=100, width = 19, font="BahnschriftLight 12", bg="#0973de", fg="#ffffff", 
                                activebackground="#0973de", activeforeground="#9e9e9e", highlightthickness=0, bd=0, borderwidth=3,relief="raised")
        self.macButton = Button(self.navLayer2Frame, height=100, width = 19, font="BahnschriftLight 12", bg="#0973de", fg="#ffffff", 
                                activebackground="#0973de", activeforeground="#9e9e9e", highlightthickness=0, bd=0, borderwidth=3,relief="raised")
        self.stpButton = Button(self.navLayer2Frame, height=100, width = 19, font="BahnschriftLight 12", bg="#0973de", fg="#ffffff", 
                                activebackground="#0973de", activeforeground="#9e9e9e", highlightthickness=0, bd=0, borderwidth=3,relief="raised")

        self.navLayer2Options = ["CAM Table Overflow", "VLAN Hopping", "DHCP Attack", "ARP Poisoning Attack", "MAC Address Spoofing", "STP Attack"]
        self.navLayer2Links = [self.showFrameCam, self.showFrameVlan, self.showFrameDhcp, self.showFrameArp, self.showFrameMac, self.showFrameStp]
        self.layer2AttackButtons = [self.camButton, self.vlanButton, self.arpButton, self.dhcpButton, self.macButton, self.stpButton]

        for i in range(len(self.navLayer2Options)):
            self.layer2AttackButtons[i].config(text=self.navLayer2Options[i])
            self.layer2AttackButtons[i].config(command=self.navLayer2Links[i])
            self.layer2AttackButtons[i].pack(side=LEFT)
        
        self.navLayer2Frame.pack_propagate(0)
        self.navLayer2Frame.pack()
        self.attackFrame.pack_propagate(0)
        self.attackFrame.pack()

        self.showFrameCam()

    def showFrameCam(self):
        self.deletePages()
        self.camFrame = Frame(self.attackFrame, width=1280, height=580, background="#0078bd")
        self.camContents = FrameCam(self.attackFrame)
        self.camFrame.pack()
        self.navLayer2Frame.update_idletasks()

        self.configureButtons("CAM Table Overflow")
    
    def showFrameVlan(self) :
        self.deletePages()
        self.vlanFrame = Frame(self.attackFrame, width=1280, height=580, background="#0078bd")
        self.vlanContents = FrameVlan(self.attackFrame)
        self.vlanFrame.pack()

        self.configureButtons("VLAN Hopping")

    def showFrameArp(self) :
        self.deletePages()
        self.arpFrame = Frame(self.attackFrame, width=1280, height=580, background="#0078bd")
        self.arpContents = FrameArp(self.attackFrame)
        self.arpFrame.pack()

        self.configureButtons("ARP Poisoning Attack")
    
    def showFrameDhcp(self):
        self.deletePages()
        self.dhcpFrame = Frame(self.attackFrame, width=1280, height=580, background="#0078bd")
        self.dhcpContents = FrameDhcp(self.attackFrame)
        self.dhcpFrame.pack()

        self.configureButtons("DHCP Attack")

    def showFrameMac(self) :
        self.deletePages()
        self.macFrame = Frame(self.attackFrame, width=1280, height=580, background="#0078bd")
        self.macContents = FrameMac(self.attackFrame)
        self.macFrame.pack()

        self.configureButtons("MAC Address Spoofing")
    
    def showFrameStp(self) :
        self.deletePages()
        self.stpFrame = Frame(self.attackFrame, width=1280, height=580, background="#0078bd")
        self.stpContents = FrameStp(self.attackFrame)
        self.stpFrame.pack()

        self.configureButtons("STP Attack")

    def configureButtons(self, buttonPressed) :
        for i in range(len(self.navLayer2Options)):
            if self.navLayer2Options[i] == buttonPressed :
                self.layer2AttackButtons[i].config(relief="sunken")
                self.layer2AttackButtons[i].config(state="disabled")
            else :
                self.layer2AttackButtons[i].config(relief="raised")
                self.layer2AttackButtons[i].config(state="normal")
                
    def deletePages(self):
        for frame in self.attackFrame.winfo_children():
            frame.destroy()