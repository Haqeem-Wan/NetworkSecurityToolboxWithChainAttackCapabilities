from tkinter import *
from DnsAttacks.PageDnsAmplification.FrameDnsAmplification import *
from DnsAttacks.PageDnsSpoofing.FrameDnsSpoofing import *

class PageDnsAttacks:
    def __init__ (self, frame):
        self.dnsAttacksFrame = frame
        self.navDnsAttacksFrame = Frame(self.dnsAttacksFrame, width=1280, height=40, background="#620387")
        self.attackFrame = Frame(self.dnsAttacksFrame, width=1280, height=630, background="#620387")

        self.dnsAmpButton = Button(self.navDnsAttacksFrame, height=100, width = 63, font="BahnschriftLight 12", bg="#8104b3", fg="#ffffff", 
                            activebackground="#8104b3", activeforeground="#9e9e9e", highlightthickness=0, bd=0, borderwidth=3, relief="raised")
        self.dnsSpoButton = Button(self.navDnsAttacksFrame, height=100, width = 63, font="BahnschriftLight 12", bg="#8104b3", fg="#ffffff", 
                            activebackground="#8104b3", activeforeground="#9e9e9e", highlightthickness=0, bd=0, borderwidth=3, relief="raised")

        self.navDnsAttacksOptions = ["DNS Amplification", "DNS Spoofing"]
        self.navDnsAttacksLinks = [self.showFrameDnsAmplification, self.showFrameDnsSpoofing]
        self.dnsAttackButtons = [self.dnsAmpButton, self.dnsSpoButton]

        for i in range(len(self.navDnsAttacksOptions)):
            self.dnsAttackButtons[i].config(text=self.navDnsAttacksOptions[i])
            self.dnsAttackButtons[i].config(command=self.navDnsAttacksLinks[i])
            self.dnsAttackButtons[i].pack(side=LEFT)

        self.navDnsAttacksFrame.pack_propagate(0)
        self.navDnsAttacksFrame.pack()
        self.attackFrame.pack_propagate(0)
        self.attackFrame.pack()

        self.showFrameDnsAmplification()

    def showFrameDnsAmplification(self):
        self.deletePages()
        self.dnsAmplificationFrame = Frame(self.attackFrame, width=1280, height=580, background="#620387")
        self.dnsAmplificationContents = FrameDnsAmplification(self.attackFrame)
        self.dnsAmplificationFrame.pack()

        self.configureButtons("DNS Amplification")
    
    def showFrameDnsSpoofing(self) :
        self.deletePages()
        self.dnsSpoofingFrame = Frame(self.attackFrame, width=1280, height=580, background="#620387")
        self.dnsSpoofingContents = FrameDnsSpoofing(self.attackFrame)
        self.dnsSpoofingFrame.pack()

        self.configureButtons("DNS Spoofing")

    def configureButtons(self, buttonPressed) :
        for i in range(len(self.navDnsAttacksOptions)):
            if self.navDnsAttacksOptions[i] == buttonPressed :
                self.dnsAttackButtons[i].config(relief="sunken")
                self.dnsAttackButtons[i].config(state="disabled")
            else :
                self.dnsAttackButtons[i].config(relief="raised")
                self.dnsAttackButtons[i].config(state="normal")

    def deletePages(self):
        for frame in self.attackFrame.winfo_children():
            frame.destroy()