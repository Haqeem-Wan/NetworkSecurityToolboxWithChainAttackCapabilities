from tkinter import *
from HttpAttacks.PageHttpManInTheMIddle.FrameHttpSessionHijacking import *

class PageHttpAttacks:
    def __init__ (self, frame):
        self.httpAttacksFrame = frame
        self.navHttpAttacksFrame = Frame(self.httpAttacksFrame, width=1280, height=40, background="#800800")
        self.attackFrame = Frame(self.httpAttacksFrame, width=1280, height=630, background="#800800")

        self.httpSessionHijackingButton = Button(self.navHttpAttacksFrame, height=100, width = 130, font="BahnschriftLight 12", bg="#bf0d00", fg="#ffffff", 
                                      activebackground="#bf0d00", activeforeground="#9e9e9e", highlightthickness=0, bd=0, borderwidth=3, relief="raised")

        self.navHttpAttacksOptions = ["HTTP Session Hijacking"]
        self.navHttpAttacksLinks = [self.showFrameHttpSessionHijacking]
        self.navHttpAttackButtons = [self.httpSessionHijackingButton]
        
        for i in range(len(self.navHttpAttacksOptions)):
            self.navHttpAttackButtons[i].config(text=self.navHttpAttacksOptions[i])
            self.navHttpAttackButtons[i].config(command=self.navHttpAttacksLinks[i])
            self.navHttpAttackButtons[i].pack(side=LEFT)

        self.navHttpAttacksFrame.pack_propagate(0)
        self.navHttpAttacksFrame.pack()
        self.attackFrame.pack_propagate(0)
        self.attackFrame.pack()

        self.showFrameHttpSessionHijacking()

    def showFrameHttpSessionHijacking(self):
        self.deletePages()
        self.httpSessionHijackingFrame = Frame(self.attackFrame, width=1280, height=580, background="#800800")
        self.httpSessionHijackingContents = FrameHttpSessionHijacking(self.attackFrame)
        self.httpSessionHijackingFrame.pack()

        self.configureButtons("HTTP Session Hijacking")

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