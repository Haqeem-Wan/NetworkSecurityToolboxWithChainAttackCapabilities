from tkinter import *
from HttpAttacks.PageSqlInjection.FrameSqlInjection import *
from HttpAttacks.PageBrokenAuth.FrameBrokenAuth import *
from HttpAttacks.PageSensitiveDataExpo.FrameSensitiveDataExpo import *
from HttpAttacks.PageXss.FrameXss import *

class PageHttpAttacks:
    def __init__ (self, frame):
        self.httpAttacksFrame = frame
        self.navHttpAttacksFrame = Frame(self.httpAttacksFrame, width=1280, height=40, background="#454545")
        self.attackFrame = Frame(self.httpAttacksFrame, width=1280, height=580, background="#454545")

        self.navHttpAttacksOptions = ["SQL Injection", "Broken Auth.", "Sensitive Data Expo.", "Cross-Site Scripting (XSS)"]
        self.navHttpAttacksLinks = [self.showFrameSqlInjection, self.showFrameBrokenAuth, 
        self.showFrameSensitiveDataExpo, self.showFrameXss]
        for i in range(len(self.navHttpAttacksOptions)):
            button = Button(self.navHttpAttacksFrame, text=self.navHttpAttacksOptions[i], height=100, width = 29, font="BahnschriftLight 12", bg="#333333", fg="#ffffff", 
            activebackground="#333333", activeforeground="#9e9e9e", highlightthickness=0, bd=0, borderwidth=3,relief="raised", 
            command=self.navHttpAttacksLinks[i])
            button.pack(side=LEFT)

        self.navHttpAttacksFrame.pack_propagate(0)
        self.navHttpAttacksFrame.pack()
        self.attackFrame.pack_propagate(0)
        self.attackFrame.pack()

    def showFrameSqlInjection(self):
        self.deletePages()
        self.synFloodingFrame = Frame(self.attackFrame, width=1280, height=580, background="#454545")
        self.synFloodingContents = FrameSqlInjection(self.attackFrame)
        self.synFloodingFrame.pack()
    
    def showFrameBrokenAuth(self) :
        self.deletePages()
        self.icmpAttacksFrame = Frame(self.attackFrame, width=1280, height=580, background="#454545")
        self.icmpAttacksContents = FrameBrokenAuth(self.attackFrame)
        self.icmpAttacksFrame.pack()

    def showFrameSensitiveDataExpo(self) :
        self.deletePages()
        self.seqNumAttacksFrame = Frame(self.attackFrame, width=1280, height=580, background="#454545")
        self.seqNumAttacksContents = FrameSensitiveDataExpo(self.attackFrame)
        self.seqNumAttacksFrame.pack()
    
    def showFrameXss(self):
        self.deletePages()
        self.tcpSessionHijackingFrame = Frame(self.attackFrame, width=1280, height=580, background="#454545")
        self.tcpSessionHijackingContents = FrameXss(self.attackFrame)
        self.tcpSessionHijackingFrame.pack()

    def deletePages(self):
        for frame in self.attackFrame.winfo_children():
            frame.destroy()