from tkinter import *
from DnsAttacks.PageDnsAmplification.FrameDnsAmplification import *
from DnsAttacks.PageDnsTunneling.FrameDnsTunneling import *
from DnsAttacks.PageDnsSpoofing.FrameDnsSpoofing import *
from DnsAttacks.PageDnsHijacking.FrameDnsHijacking import *

class PageDnsAttacks:
    def __init__ (self, frame):
        self.dnsAttacksFrame = frame
        self.navDnsAttacksFrame = Frame(self.dnsAttacksFrame, width=1280, height=40, background="#454545")
        self.attackFrame = Frame(self.dnsAttacksFrame, width=1280, height=580, background="#454545")

        self.navDnsAttacksOptions = ["DNS Amplification", "DNS Tunneling", "DNS Spoofing", "DNS Hijacking"]
        self.navDnsAttacksLinks = [self.showFrameDnsAmplification, self.showFrameDnsTunneling, self.showFrameDnsSpoofing, 
        self.showFrameDnsHijacking]
        for i in range(len(self.navDnsAttacksOptions)):
            button = Button(self.navDnsAttacksFrame, text=self.navDnsAttacksOptions[i], height=100, width = 29, font="BahnschriftLight 12", bg="#333333", fg="#ffffff", 
            activebackground="#333333", activeforeground="#9e9e9e", highlightthickness=0, bd=0, borderwidth=3,relief="raised*-*/////////////////////////////////////////////////", 
            command=self.navDnsAttacksLinks[i])
            button.pack(side=LEFT)

        self.navDnsAttacksFrame.pack_propagate(0)
        self.navDnsAttacksFrame.pack()
        self.attackFrame.pack_propagate(0)
        self.attackFrame.pack()

        self.testLabel = Label(self.dnsAttacksFrame, text="DNS", fg="#ffffff", font="bahnschrift 15")
        self.testLabel.pack()

    def showFrameDnsAmplification(self):
        self.deletePages()
        self.dnsAmplificationFrame = Frame(self.attackFrame, width=1280, height=580, background="#454545")
        self.dnsAmplificationContents = FrameDnsAmplification(self.attackFrame)
        self.dnsAmplificationFrame.pack()
    
    def showFrameDnsTunneling(self) :
        self.deletePages()
        self.dnsTunnelingFrame = Frame(self.attackFrame, width=1280, height=580, background="#454545")
        self.dnsTunnelingContents = FrameDnsTunneling(self.attackFrame)
        self.dnsTunnelingFrame.pack()

    def showFrameDnsSpoofing(self) :
        self.deletePages()
        self.dnsSpoofingFrame = Frame(self.attackFrame, width=1280, height=580, background="#454545")
        self.dnsSpoofingContents = FrameDnsSpoofing(self.attackFrame)
        self.dnsSpoofingFrame.pack()
    
    def showFrameDnsHijacking(self):
        self.deletePages()
        self.dnsHijackingFrame = Frame(self.attackFrame, width=1280, height=580, background="#454545")
        self.dnsHijackingContents = FrameDnsHijacking(self.attackFrame)
        self.dnsHijackingFrame.pack()

    def deletePages(self):
        for frame in self.attackFrame.winfo_children():
            frame.destroy()