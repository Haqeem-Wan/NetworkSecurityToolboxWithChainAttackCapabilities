from tkinter import *
from WifiHacking.PageDos.FrameDos import *
from WifiHacking.PageEvilTwinAttack.FrameEvilTwinAttack import *
from WifiHacking.PageWpaWpa2Cracking.FrameWpaWpa2Cracking import *

class PageWifiHacking:
    def __init__ (self, frame):
        self.wifiHackingFrame = frame
        self.navWifiHackingFrame = Frame(self.wifiHackingFrame, width=1280, height=40, background="#454545")
        self.attackFrame = Frame(self.wifiHackingFrame, width=1280, height=580, background="#454545")

        self.navWifiHackingOptions = ["Denial of Service (DoS)", "Evil Twin Attack", "WPA / WPA2 Cracking"]
        self.navWifiHackingLinks = [self.showFrameDos, self.showFrameEvilTwinAttack, self.showFrameWpaWpa2Cracking]
        for i in range(len(self.navWifiHackingOptions)):
            button = Button(self.navWifiHackingFrame, text=self.navWifiHackingOptions[i], height=100, width = 40, font="BahnschriftLight 12", bg="#333333", fg="#ffffff", 
            activebackground="#333333", activeforeground="#9e9e9e", highlightthickness=0, bd=0, borderwidth=3,relief="raised", 
            command=self.navWifiHackingLinks[i])
            button.pack(side=LEFT)

        self.navWifiHackingFrame.pack_propagate(0)
        self.navWifiHackingFrame.pack()
        self.attackFrame.pack_propagate(0)
        self.attackFrame.pack()

    def showFrameDos(self):
        self.deletePages()
        self.dosFrame = Frame(self.attackFrame, width=1280, height=580, background="#454545")
        self.synFloodingContents = FrameDos(self.attackFrame)
        self.dosFrame.pack()
    
    def showFrameEvilTwinAttack(self) :
        self.deletePages()
        self.evilTwinAttackFrame = Frame(self.attackFrame, width=1280, height=580, background="#454545")
        self.icmpAttacksContents = FrameEvilTwinAttack(self.attackFrame)
        self.evilTwinAttackFrame.pack()

    def showFrameWpaWpa2Cracking(self) :
        self.deletePages()
        self.wpaWpa2CrackingFrame = Frame(self.attackFrame, width=1280, height=580, background="#454545")
        self.seqNumAttacksContents = FrameWpaWpa2Cracking(self.attackFrame)
        self.wpaWpa2CrackingFrame.pack()

    def deletePages(self):
        for frame in self.attackFrame.winfo_children():
            frame.destroy()