from tkinter import *
from WifiHacking.PageWpaWpa2Cracking.FrameWpaWpa2Cracking import *

class PageWifiHacking:
    def __init__ (self, frame):
        self.wifiHackingFrame = frame
        self.navWifiHackingFrame = Frame(self.wifiHackingFrame, width=1280, height=40, background="#87005d")
        self.attackFrame = Frame(self.wifiHackingFrame, width=1280, height=630, background="#87005d")

        self.wpaWpa2Button = Button(self.navWifiHackingFrame, height=100, width = 130, font="BahnschriftLight 12", bg="#b3007b", fg="#ffffff", 
                                    activebackground="#b3007b", activeforeground="#9e9e9e", highlightthickness=0, bd=0, borderwidth=3,relief="raised")

        self.navWifiHackingOptions = ["WPA / WPA2 Cracking"]
        self.navWifiHackingLinks = [self.showFrameWpaWpa2Cracking]
        self.navWifiHackingButtons = [self.wpaWpa2Button]
        
        for i in range(len(self.navWifiHackingOptions)):
            self.navWifiHackingButtons[i].config(text=self.navWifiHackingOptions[i])
            self.navWifiHackingButtons[i].config(command=self.navWifiHackingLinks[i])
            self.navWifiHackingButtons[i].pack(side=LEFT)

        self.navWifiHackingFrame.pack_propagate(0)
        self.navWifiHackingFrame.pack()
        self.attackFrame.pack_propagate(0)
        self.attackFrame.pack()

        self.showFrameWpaWpa2Cracking()

    def showFrameWpaWpa2Cracking(self) :
        self.deletePages()
        self.wpaWpa2CrackingFrame = Frame(self.attackFrame, width=1280, height=580, background="#87005d")
        self.seqNumAttacksContents = FrameWpaWpa2Cracking(self.attackFrame)
        self.wpaWpa2CrackingFrame.pack()

        self.configureButtons("WPA / WPA2 Cracking")

    def configureButtons(self, buttonPressed) :
        for i in range(len(self.navWifiHackingOptions)):
            if self.navWifiHackingOptions[i] == buttonPressed :
                self.navWifiHackingButtons[i].config(relief="sunken")
                self.navWifiHackingButtons[i].config(state="disabled")
            else :
                self.navWifiHackingButtons[i].config(relief="raised")
                self.navWifiHackingButtons[i].config(state="normal")
  
    def deletePages(self):
        for frame in self.attackFrame.winfo_children():
            frame.destroy()