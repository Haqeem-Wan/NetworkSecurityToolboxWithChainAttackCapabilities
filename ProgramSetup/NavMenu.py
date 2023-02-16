from tkinter import *
import PIL.Image
import PIL.ImageTk
from Home.PageHome import *
from Layer2Attacks.PageLayer2Attacks import *
from TcpIpAttacks.PageTcpIpAttacks import *
from DnsAttacks.PageDnsAttacks import *
from HttpAttacks.PageHttpAttacks import *
from WifiHacking.PageWifiHacking import *

class NavMenu:
    def __init__ (self, root, headerFrame, navMenuFrame, contentFrame):
        self.root = root
        self.headerFrame = headerFrame
        self.navMenuFrame = navMenuFrame
        self.contentFrame = contentFrame

        self.closedNavMenuImg = PIL.Image.open("NetworkSecurityToolboxWithChainAttackCapabilities/img/Closed_Box.png")
        self.openNavMenuImg = PIL.Image.open("NetworkSecurityToolboxWithChainAttackCapabilities/img/Open_Box.png")

        self.closedNavMenuImg = self.closedNavMenuImg.resize((30,30))
        self.openNavMenuImg = self.openNavMenuImg.resize((35,30))

        self.closedNavMenuIcon = PIL.ImageTk.PhotoImage(self.closedNavMenuImg)
        self.openNavMenuIcon = PIL.ImageTk.PhotoImage(self.openNavMenuImg)

        self.navMenuOpen = False

        self.openNavMenuButton = Button(self.headerFrame, bd=0, image=self.closedNavMenuIcon, bg="#333333", 
        activebackground="#333333", padx=20, highlightthickness=0, command=self.toggleNavMenu)
        self.openNavMenuButton.place(x=10,y=7)

        self.showPageHome()

        y = 80
        self.mainMenuOptions = ["Home", "Layer 2 Attacks", "TCP / IP Attacks", "DNS Attacks", "HTTP Attacks", "Wifi Hacking"]
        self.mainMenuLinks = [self.showPageHome, self.showPageLayer2Attacks, self.showPageTcpIpAttacks, self.showPageDnsAttacks, self.showPageHttpAttacks, self.showPageWifiHacking]
        for i in range(len(self.mainMenuOptions)):
            Button(self.navMenuFrame, text=self.mainMenuOptions[i], font="BahnschriftLight 15", bg="#333333", fg="#ffffff", 
            activebackground="#333333", activeforeground="#9e9e9e", highlightthickness=0, bd=0, command=self.mainMenuLinks[i]).place(x=25,y=y)
            y += 100

        self.closeNavMenuButton = Button(self.navMenuFrame, image=self.openNavMenuIcon, bg="#333333", 
        activebackground="#333333", padx=20, highlightthickness=0, command=self.toggleNavMenu)
        self.closeNavMenuButton.place(x=250, y=7)

    def toggleNavMenu(self):
        if self.navMenuOpen is True:
            for x in range (0, 301, 4):
                self.navMenuFrame.place(x=-x, y=0)
                self.headerFrame.update()

            self.navMenuOpen = False

        else:
            for x in range(-300, 0, 3):
                self.navMenuFrame.place(x=x, y=0)
                self.headerFrame.update()

            self.navMenuOpen = True

    def showPageHome(self):
        self.deletePages()
        self.homeFrame = Frame(self.contentFrame, width=1280, height=300, background="#454545")
        self.homeContents = PageHome(self.homeFrame)
        self.homeFrame.pack()
    
    def showPageLayer2Attacks(self) :
        self.deletePages()
        self.layer2Frame = Frame(self.contentFrame, width=1280, height=620, background="#454545")
        self.layer2Contents = PageLayer2Attacks(self.layer2Frame)
        self.layer2Frame.pack()
    
    def showPageTcpIpAttacks(self) :
        self.deletePages()
        self.tcpFrame = Frame(self.contentFrame, width=1280, height=620, background="#454545")
        self.tcpContents = PageTcpIpAttacks(self.tcpFrame)
        self.tcpFrame.pack()
    
    def showPageDnsAttacks(self) :
        self.deletePages()
        self.dnsFrame = Frame(self.contentFrame, width=1280, height=620, background="#454545")
        self.dnsContents = PageDnsAttacks(self.dnsFrame)
        self.dnsFrame.pack()
    
    def showPageHttpAttacks(self) :
        self.deletePages()
        self.httpFrame = Frame(self.contentFrame, width=1280, height=620, background="#454545")
        self.httpContents = PageHttpAttacks(self.httpFrame)
        self.httpFrame.pack()
    
    def showPageWifiHacking(self) :
        self.deletePages()
        self.wifiFrame = Frame(self.contentFrame, width=1280, height=620, background="#454545")
        self.wifiContents = PageWifiHacking(self.wifiFrame)
        self.wifiFrame.pack()

    def deletePages(self):
        for frame in self.contentFrame.winfo_children():
            frame.destroy()