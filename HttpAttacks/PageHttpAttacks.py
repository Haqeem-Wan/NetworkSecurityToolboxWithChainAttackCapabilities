from tkinter import *
from HttpAttacks.PageSqlInjection.FrameSqlInjection import *
from HttpAttacks.PageBrokenAuth.FrameBrokenAuth import *
from HttpAttacks.PageSensitiveDataExpo.FrameSensitiveDataExpo import *
from HttpAttacks.PageXss.FrameXss import *

class PageHttpAttacks:
    def __init__ (self, frame):
        self.httpAttacksFrame = frame
        self.navHttpAttacksFrame = Frame(self.httpAttacksFrame, width=1280, height=40, background="#454545")
        self.attackFrame = Frame(self.httpAttacksFrame, width=1280, height=630, background="#454545")

        self.sqlInjectButton = Button(self.navHttpAttacksFrame, height=100, width = 29, font="BahnschriftLight 12", bg="#333333", fg="#ffffff", 
                                      activebackground="#333333", activeforeground="#9e9e9e", highlightthickness=0, bd=0, borderwidth=3, relief="raised")
        self.brokenAuthButton = Button(self.navHttpAttacksFrame, height=100, width = 29, font="BahnschriftLight 12", bg="#333333", fg="#ffffff", 
                                       activebackground="#333333", activeforeground="#9e9e9e", highlightthickness=0, bd=0, borderwidth=3, relief="raised")
        self.senDataExpButton = Button(self.navHttpAttacksFrame, height=100, width = 29, font="BahnschriftLight 12", bg="#333333", fg="#ffffff", 
                                       activebackground="#333333", activeforeground="#9e9e9e", highlightthickness=0, bd=0, borderwidth=3, relief="raised")
        self.xssButton = Button(self.navHttpAttacksFrame, height=100, width = 29, font="BahnschriftLight 12", bg="#333333", fg="#ffffff", 
                                activebackground="#333333", activeforeground="#9e9e9e", highlightthickness=0, bd=0, borderwidth=3, relief="raised")

        self.navHttpAttacksOptions = ["SQL Injection", "Broken Auth.", "Sensitive Data Expo.", "Cross-Site Scripting (XSS)"]
        self.navHttpAttacksLinks = [self.showFrameSqlInjection, self.showFrameBrokenAuth, 
        self.showFrameSensitiveDataExpo, self.showFrameXss]
        self.navHttpAttackButtons = [self.sqlInjectButton, self.brokenAuthButton, self.senDataExpButton, self.xssButton]
        
        for i in range(len(self.navHttpAttacksOptions)):
            self.navHttpAttackButtons[i].config(text=self.navHttpAttacksOptions[i])
            self.navHttpAttackButtons[i].config(command=self.navHttpAttacksLinks[i])
            self.navHttpAttackButtons[i].pack(side=LEFT)

        self.navHttpAttacksFrame.pack_propagate(0)
        self.navHttpAttacksFrame.pack()
        self.attackFrame.pack_propagate(0)
        self.attackFrame.pack()

    def showFrameSqlInjection(self):
        self.deletePages()
        self.synFloodingFrame = Frame(self.attackFrame, width=1280, height=580, background="#454545")
        self.synFloodingContents = FrameSqlInjection(self.attackFrame)
        self.synFloodingFrame.pack()

        self.configureButtons("SQL Injection")
    
    def showFrameBrokenAuth(self) :
        self.deletePages()
        self.icmpAttacksFrame = Frame(self.attackFrame, width=1280, height=580, background="#454545")
        self.icmpAttacksContents = FrameBrokenAuth(self.attackFrame)
        self.icmpAttacksFrame.pack()

        self.configureButtons("Broken Auth.")

    def showFrameSensitiveDataExpo(self) :
        self.deletePages()
        self.seqNumAttacksFrame = Frame(self.attackFrame, width=1280, height=580, background="#454545")
        self.seqNumAttacksContents = FrameSensitiveDataExpo(self.attackFrame)
        self.seqNumAttacksFrame.pack()

        self.configureButtons("Sensitive Data Expo.")
    
    def showFrameXss(self):
        self.deletePages()
        self.tcpSessionHijackingFrame = Frame(self.attackFrame, width=1280, height=580, background="#454545")
        self.tcpSessionHijackingContents = FrameXss(self.attackFrame)
        self.tcpSessionHijackingFrame.pack()

        self.configureButtons("Cross-Site Scripting (XSS)")

    def configureButtons(self, buttonPressed) :
        for i in range(len(self.navHttpAttacksOptions)):
            if self.navHttpAttacksOptions[i] == buttonPressed :
                self.navHttpAttackButtons[i].config(relief="sunken")
                self.navHttpAttackButtons[i].config(state="disabled")
            else :
                self.navHttpAttackButtons[i].config(relief="raised")
                self.navHttpAttackButtons[i].config(state="normal")
    

    def deletePages(self):
        for frame in self.attackFrame.winfo_children():
            frame.destroy()