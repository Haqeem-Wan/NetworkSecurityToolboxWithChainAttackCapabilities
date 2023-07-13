from tkinter import *
from tkinter.ttk import Combobox, Style
import threading

from Layer2Attacks.PageCamAttacks.FrameCam import *
from Layer2Attacks.PageDhcpAttacks.FrameDhcp import *
from Layer2Attacks.PageArpAttacks.FrameArp import *
from Layer2Attacks.PageMacAttacks.FrameMac import *

from TcpIpAttacks.PageSynFlooding.FrameSynFlooding import *
from TcpIpAttacks.PageIcmpAttacks.FrameIcmpAttacks import *

from DnsAttacks.PageDnsAmplification.FrameDnsAmplification import *
from DnsAttacks.PageDnsSpoofing.FrameDnsSpoofing import *

from HttpAttacks.PageHttpMitm.FrameHttpMitm import *

from WifiHacking.PageWpaWpa2Cracking.FrameWpaWpa2Cracking import *

class PageChainAttacks :
    def __init__ (self, frame) :
        self.chainAttacksFrame = frame
        self.attackDirectoryFrame = Frame(self.chainAttacksFrame, width=1280, height=110, 
                                          background="#833301", borderwidth=3, relief="raised")
        self.attacksFrame = Frame(self.chainAttacksFrame, width=1280, height = 600, 
                                  background="#AC4201")

        self.attacksScrollCanvas = Canvas(self.attacksFrame, width=500, height=600, background="#AC4201", yscrollincrement=8)
        self.attacksScrollCanvas.pack(side=LEFT, fill=BOTH, expand=1)
        
        # Create Attack Directory Dropdown
        self.attackDirectoryStyle = Style()
        if not self.attackDirectoryStyle.theme_names().__contains__("attackDirectoryTheme") :
            self.attackDirectoryStyle.theme_create("attackDirectoryTheme", parent="alt",
                                                settings = {"TCombobox" : {
                                                        "configure" : {
                                                            "selectbackground" : "transparent",
                                                            "fieldbackground" : "#E0986B",
                                                            "background" : "#612601",
                                                            "selectforeground" : "#000000"
                                                }}})
        self.attackDirectoryStyle.theme_use("attackDirectoryTheme")
        
        self.attackDirectorySelected = StringVar()
        
        self.attackDirectoryDropdown = Combobox(self.attackDirectoryFrame, width=25, 
                                                textvariable=self.attackDirectorySelected, justify="center")
        self.attackDirectoryDropdown["state"] = "readonly"
        self.attackDirectoryDropdown.bind("<<ComboboxSelected>>", self.switchAttackTypes)
        
        self.attackDirectoryDropdown['values'] = (
            "Layer 2 Attacks",
            "TCP / IP attacks",
            "DNS Attacks",
            "HTTP Attacks",
            "Wifi Hacking"
            )
        
        # Create Attack Type Dropdown
        self.attackTypeSelected = StringVar()
        
        self.attackTypeDropdown = Combobox(self.attackDirectoryFrame, width=25, 
                                                      textvariable=self.attackTypeSelected, justify="center")
        self.attackTypeDropdown["state"] = "readonly"
        
        self.attackTypeDropdown['values'] = (
            "CAM Table Overflow",
            "DHCP Starvation Attack",
            "ARP Poisoning Attack",
            "MAC Address Spoofing"
            )
        
        self.addAttackTypeButton = Button(self.attackDirectoryFrame, height=2, width=5, font="bahnschrift 15", 
                                          text="Add", fg="#ffffff", bg="#612601", command=lambda : self.addAttackTypeFrame(self.attackTypeDropdown.get()))

        # Create Scrollbar for Attack Type Frame
        self.attackTypeScrollbar = Scrollbar(self.attacksFrame, orient=VERTICAL, command=self.attacksScrollCanvas.yview)
        self.attackTypeScrollbar.pack(side = RIGHT, fill = Y)

        self.attacksScrollCanvas.configure(yscrollcommand=self.attackTypeScrollbar.set)
        self.attacksScrollCanvas.bind("<Configure>", lambda e : self.attacksScrollCanvas.configure(scrollregion=self.attacksScrollCanvas.bbox("all")))
        self.attacksScrollCanvas.bind_all("<MouseWheel>", lambda e : self.attacksScrollCanvas.yview_scroll(-1, "units"))

        self.attacksScrollFrame = Frame(self.attacksScrollCanvas, background="#252525", highlightbackground="#ffffff")
        self.attacksScrollCanvas.create_window((0,0), window = self.attacksScrollFrame, anchor = NW)
        self.attacksScrollFrame.bind("<Configure>", lambda e : self.attacksScrollCanvas.configure(scrollregion=self.attacksScrollCanvas.bbox("all")))

        self.chosenAttackTypes = []

        self.executeChainAttackButton = Button(self.attacksScrollFrame, height=2, width=96, font="bahnschrift 15", 
                                          text="Execute Chain Attack!", fg="#ffffff", bg="#771902", command = lambda : self.executeChainAttack())

        self.terminateChainAttackButton = Button(self.attacksScrollFrame, height=2, width=96, font="bahnschrift 15", 
                                          text="Terminate Chain Attack!", fg="#ffffff", bg="#771902", command = lambda : self.terminateChainAttack())
        
        self.terminateChainAttackButton.pack(side=BOTTOM, fill = X)
        self.executeChainAttackButton.pack(side=BOTTOM, fill = X)

        self.attackDirectoryDropdown.current(0)
        self.attackDirectoryDropdown.place(x=300, y=40)

        self.attackTypeDropdown.current(0)
        self.attackTypeDropdown.place(x=600, y=40)

        self.addAttackTypeButton.place(x=900, y=20)

        self.attackDirectoryFrame.pack_propagate(0)
        self.attackDirectoryFrame.pack()
        self.attacksFrame.pack_propagate(0)
        self.attacksFrame.pack()

    def switchAttackTypes(self, event) :
        self.chosenDirectory = self.attackDirectoryDropdown.get()
        if self.chosenDirectory == "Layer 2 Attacks" :
            self.attackTypeDropdown['values'] = (
                "CAM Table Overflow",
                "DHCP Starvation Attack",
                "ARP Poisoning Attack",
                "MAC Address Spoofing",
            )
            self.attackTypeDropdown.current(0)
        elif self.chosenDirectory == "TCP / IP attacks" :
            self.attackTypeDropdown['values'] = (
                "Syn Flooding",
                "ICMP Attack",
            )
            self.attackTypeDropdown.current(0)
        elif self.chosenDirectory == "DNS Attacks" :
            self.attackTypeDropdown['values'] = (
                "DNS Amplification",
                "DNS Spoofing",
            )
            self.attackTypeDropdown.current(0)
        elif self.chosenDirectory == "HTTP Attacks" :
            self.attackTypeDropdown['values'] = (
                "HTTP-Man-In-The-Middle"
            )
            self.attackTypeDropdown.current(0)
        elif self.chosenDirectory == "Wifi Hacking" :
            self.attackTypeDropdown['values'] = (
                "WPA/WPA2-Cracking"
            )
            self.attackTypeDropdown.current(0)

    def addAttackTypeFrame(self, chosenAttackType) :
        if chosenAttackType == "CAM Table Overflow" :
            camFrame = Frame(self.attacksScrollFrame, width=1280, height=200, background="#612601", borderwidth=3, relief="raised")
            camFrame.pack()

            camLabel = Label(camFrame, text=" CAM Table Overflow ", fg="#ffffff", bg="#2E1201", font="bahnschrift 12")
            camLabel.place(x=0, y=0)

            camTargetIpLabel = Label(camFrame, text="Target IP Address                    :", fg="#ffffff", bg="#612601", font="bahnschrift 12")
            camTargetIpLabel.place(x = 10, y = 70)

            self.camTargetIpEntry = Entry(camFrame, width = 20, font="bahnschrift 12", fg="#ffffff", bg="#252525")
            self.camTargetIpEntry.place(x = 300, y = 70)

            camPacketNumberLabel = Label(camFrame, text="Number of Packets to send     :", fg="#ffffff", bg="#612601", font="bahnschrift 12")
            camPacketNumberLabel.place(x = 10, y = 120)

            self.camPacketNumberEntry = Entry(camFrame, width = 20, font="bahnschrift 12", fg="#ffffff", bg="#252525")
            self.camPacketNumberEntry.place(x = 300, y = 120)



            camTerminalLabel = Label(camFrame, text="Terminal", fg="#ffffff", bg="#612601", font="bahnschrift 15")
            camTerminalLabel.place(x = 660, y = 20)

            camTerminalFrame = Frame(camFrame, width=300, height=120, background="#252525", highlightbackground="#ffffff", highlightthickness=2)
            camTerminalFrame.pack_propagate(False)
            camTerminalFrame.place(x = 555, y = 55)

            camTerminalScrollCanvas = Canvas(camTerminalFrame, background="#252525", highlightbackground="#ffffff", yscrollincrement=8)
            camTerminalScrollCanvas.pack(side = LEFT, fill = BOTH, expand = 1)
        
            camTerminalVerticalScrollbar = Scrollbar(camTerminalScrollCanvas, orient=VERTICAL, command = camTerminalScrollCanvas.yview)
            camTerminalVerticalScrollbar.pack(side = RIGHT, fill = Y)

            camTerminalHorizontalScrollbar = Scrollbar(camTerminalScrollCanvas, orient=HORIZONTAL, command = camTerminalScrollCanvas.xview)
            camTerminalHorizontalScrollbar.pack(side = BOTTOM, fill = X)

            camTerminalScrollCanvas.configure(yscrollcommand=camTerminalVerticalScrollbar.set)
            camTerminalScrollCanvas.bind("<Configure>", lambda e : camTerminalScrollCanvas.configure(scrollregion=camTerminalScrollCanvas.bbox("all")))
            camTerminalScrollCanvas.bind_all("<MouseWheel>", lambda e : camTerminalScrollCanvas.yview_scroll(-1, "units"))

            camTerminalScrollCanvas.configure(xscrollcommand=camTerminalHorizontalScrollbar.set)
            camTerminalScrollCanvas.bind("<Configure>", lambda e : camTerminalScrollCanvas.configure(scrollregion=camTerminalScrollCanvas.bbox("all")))
            camTerminalScrollCanvas.bind_all("<MouseWheel>", lambda e : camTerminalScrollCanvas.xview_scroll(-1, "units"))

            self.camTerminalContentFrame = Frame(camTerminalScrollCanvas, background="#252525", highlightbackground="#ffffff")
            camTerminalScrollCanvas.create_window((0,0), window = self.camTerminalContentFrame, anchor = NW)
            self.camTerminalContentFrame.bind("<Configure>", lambda e : camTerminalScrollCanvas.configure(scrollregion=camTerminalScrollCanvas.bbox("all")))



            camErrorLabel = Label(camFrame, text="Errors", fg="#ffffff", bg="#612601", font="bahnschrift 15")
            camErrorLabel.place(x = 1035, y = 20)

            camErrorOutputFrame = Frame(camFrame, width=300, height=120, background="#252525", highlightbackground="#ffffff", highlightthickness=2)
            camErrorOutputFrame.pack_propagate(False)
            camErrorOutputFrame.place(x = 915, y = 55)

            camErrorOutputScrollCanvas = Canvas(camErrorOutputFrame, background="#252525", highlightbackground="#ffffff", yscrollincrement=8)
            camErrorOutputScrollCanvas.pack(side = LEFT, fill = BOTH, expand=1)
        
            camErrorOutputVerticalScrollbar = Scrollbar(camErrorOutputScrollCanvas, orient=VERTICAL, command = camErrorOutputScrollCanvas.yview)
            camErrorOutputVerticalScrollbar.pack(side = RIGHT, fill = Y)

            camErrorOutputHorizontalScrollbar = Scrollbar(camErrorOutputScrollCanvas, orient=HORIZONTAL, command = camErrorOutputScrollCanvas.xview)
            camErrorOutputHorizontalScrollbar.pack(side = BOTTOM, fill = X)

            camErrorOutputScrollCanvas.configure(yscrollcommand=camErrorOutputVerticalScrollbar.set)
            camErrorOutputScrollCanvas.bind("<Configure>", lambda e : camErrorOutputScrollCanvas.configure(scrollregion=camErrorOutputScrollCanvas.bbox("all")))
            camErrorOutputFrame.bind_all("<MouseWheel>", lambda e : camErrorOutputScrollCanvas.yview_scroll(-1, "units"))

            camErrorOutputScrollCanvas.configure(xscrollcommand=camErrorOutputHorizontalScrollbar.set)
            camErrorOutputScrollCanvas.bind("<Configure>", lambda e : camErrorOutputScrollCanvas.configure(scrollregion=camErrorOutputScrollCanvas.bbox("all")))
            camErrorOutputFrame.bind_all("<MouseWheel>", lambda e : camErrorOutputScrollCanvas.xview_scroll(-1, "units"))

            self.camErrorOutputContentFrame = Frame(camErrorOutputScrollCanvas, background="#252525", highlightbackground="#ffffff")
            camErrorOutputScrollCanvas.create_window((0,0), window = self.camErrorOutputContentFrame, anchor = NW)
            self.camErrorOutputContentFrame.bind("<Configure>", lambda e : camErrorOutputScrollCanvas.configure(scrollregion=camErrorOutputScrollCanvas.bbox("all")))
            
        elif chosenAttackType == "DHCP Starvation Attack" :
            dhcpAttackFrame = Frame(self.attacksScrollFrame, width=1280, height=200, background="#612601", borderwidth=3, relief="raised")
            dhcpAttackFrame.pack()

            dhcpAttackLabel = Label(dhcpAttackFrame, text=" DHCP Starvation Attack ", fg="#ffffff", bg="#2E1201", font="bahnschrift 12")
            dhcpAttackLabel.place(x=0, y=0)

            dhcpAttackInterfaceLabel = Label(dhcpAttackFrame, text="Interface               :", fg="#ffffff", bg="#612601", font="bahnschrift 12")
            dhcpAttackInterfaceLabel.place(x = 10, y = 100)

            self.dhcpAttackInterfaceEntry = Entry(dhcpAttackFrame, width = 20, font="bahnschrift 12", fg="#ffffff", bg="#252525")
            self.dhcpAttackInterfaceEntry.place(x = 300, y = 100)



            dhcpAttackTerminalLabel = Label(dhcpAttackFrame, text="Terminal", fg="#ffffff", bg="#612601", font="bahnschrift 15")
            dhcpAttackTerminalLabel.place(x = 660, y = 20)

            dhcpAttackTerminalFrame = Frame(dhcpAttackFrame, width=300, height=120, background="#252525", highlightbackground="#ffffff", highlightthickness=2)
            dhcpAttackTerminalFrame.pack_propagate(False)
            dhcpAttackTerminalFrame.place(x = 555, y = 55)

            dhcpAttackTerminalScrollCanvas = Canvas(dhcpAttackTerminalFrame, background="#252525", highlightbackground="#ffffff", yscrollincrement=8)
            dhcpAttackTerminalScrollCanvas.pack(side = LEFT, fill = BOTH, expand = 1)
        
            dhcpAttackTerminalVerticalScrollbar = Scrollbar(dhcpAttackTerminalScrollCanvas, orient=VERTICAL, command = dhcpAttackTerminalScrollCanvas.yview)
            dhcpAttackTerminalVerticalScrollbar.pack(side = RIGHT, fill = Y)

            dhcpAttackTerminalHorizontalScrollbar = Scrollbar(dhcpAttackTerminalScrollCanvas, orient=HORIZONTAL, command = dhcpAttackTerminalScrollCanvas.xview)
            dhcpAttackTerminalHorizontalScrollbar.pack(side = BOTTOM, fill = X)

            dhcpAttackTerminalScrollCanvas.configure(yscrollcommand=dhcpAttackTerminalVerticalScrollbar.set)
            dhcpAttackTerminalScrollCanvas.bind("<Configure>", lambda e : dhcpAttackTerminalScrollCanvas.configure(scrollregion=dhcpAttackTerminalScrollCanvas.bbox("all")))
            dhcpAttackTerminalScrollCanvas.bind_all("<MouseWheel>", lambda e : dhcpAttackTerminalScrollCanvas.yview_scroll(-1, "units"))

            dhcpAttackTerminalScrollCanvas.configure(xscrollcommand=dhcpAttackTerminalHorizontalScrollbar.set)
            dhcpAttackTerminalScrollCanvas.bind("<Configure>", lambda e : dhcpAttackTerminalScrollCanvas.configure(scrollregion=dhcpAttackTerminalScrollCanvas.bbox("all")))
            dhcpAttackTerminalScrollCanvas.bind_all("<MouseWheel>", lambda e : dhcpAttackTerminalScrollCanvas.xview_scroll(-1, "units"))

            self.dhcpAttackTerminalContentFrame = Frame(dhcpAttackTerminalScrollCanvas, background="#252525", highlightbackground="#ffffff")
            dhcpAttackTerminalScrollCanvas.create_window((0,0), window = self.dhcpAttackTerminalContentFrame, anchor = NW)
            self.dhcpAttackTerminalContentFrame.bind("<Configure>", lambda e : dhcpAttackTerminalScrollCanvas.configure(scrollregion=dhcpAttackTerminalScrollCanvas.bbox("all")))



            dhcpAttackErrorLabel = Label(dhcpAttackFrame, text="Errors", fg="#ffffff", bg="#612601", font="bahnschrift 15")
            dhcpAttackErrorLabel.place(x = 1035, y = 20)

            dhcpAttackErrorOutputFrame = Frame(dhcpAttackFrame, width=300, height=120, background="#252525", highlightbackground="#ffffff", highlightthickness=2)
            dhcpAttackErrorOutputFrame.pack_propagate(False)
            dhcpAttackErrorOutputFrame.place(x = 915, y = 55)

            dhcpAttackErrorOutputScrollCanvas = Canvas(dhcpAttackErrorOutputFrame, background="#252525", highlightbackground="#ffffff", yscrollincrement=8)
            dhcpAttackErrorOutputScrollCanvas.pack(side = LEFT, fill = BOTH, expand=1)
        
            dhcpAttackErrorOutputVerticalScrollbar = Scrollbar(dhcpAttackErrorOutputScrollCanvas, orient=VERTICAL, command = dhcpAttackErrorOutputScrollCanvas.yview)
            dhcpAttackErrorOutputVerticalScrollbar.pack(side = RIGHT, fill = Y)

            dhcpAttackErrorOutputHorizontalScrollbar = Scrollbar(dhcpAttackErrorOutputScrollCanvas, orient=HORIZONTAL, command = dhcpAttackErrorOutputScrollCanvas.xview)
            dhcpAttackErrorOutputHorizontalScrollbar.pack(side = BOTTOM, fill = X)

            dhcpAttackErrorOutputScrollCanvas.configure(yscrollcommand=dhcpAttackErrorOutputVerticalScrollbar.set)
            dhcpAttackErrorOutputScrollCanvas.bind("<Configure>", lambda e : dhcpAttackErrorOutputScrollCanvas.configure(scrollregion=dhcpAttackErrorOutputScrollCanvas.bbox("all")))
            dhcpAttackErrorOutputFrame.bind_all("<MouseWheel>", lambda e : dhcpAttackErrorOutputScrollCanvas.yview_scroll(-1, "units"))

            dhcpAttackErrorOutputScrollCanvas.configure(xscrollcommand=dhcpAttackErrorOutputHorizontalScrollbar.set)
            dhcpAttackErrorOutputScrollCanvas.bind("<Configure>", lambda e : dhcpAttackErrorOutputScrollCanvas.configure(scrollregion=dhcpAttackErrorOutputScrollCanvas.bbox("all")))
            dhcpAttackErrorOutputFrame.bind_all("<MouseWheel>", lambda e : dhcpAttackErrorOutputScrollCanvas.xview_scroll(-1, "units"))

            self.dhcpAttackErrorOutputContentFrame = Frame(dhcpAttackErrorOutputScrollCanvas, background="#252525", highlightbackground="#ffffff")
            dhcpAttackErrorOutputScrollCanvas.create_window((0,0), window = self.dhcpAttackErrorOutputContentFrame, anchor = NW)
            self.dhcpAttackErrorOutputContentFrame.bind("<Configure>", lambda e : dhcpAttackErrorOutputScrollCanvas.configure(scrollregion=dhcpAttackErrorOutputScrollCanvas.bbox("all")))

        elif chosenAttackType == "ARP Poisoning Attack" :
            arpPoisonFrame = Frame(self.attacksScrollFrame, width=1280, height=200, background="#612601", borderwidth=3, relief="raised")
            arpPoisonFrame.pack()

            arpPoisonLabel = Label(arpPoisonFrame, text=" ARP Poisoning Attack ", fg="#ffffff", bg="#2E1201", font="bahnschrift 12")
            arpPoisonLabel.place(x=0, y=0)

            arpPoisonTargetIpLabel = Label(arpPoisonFrame, text="Target IP Address                   :", fg="#ffffff", bg="#612601", font="bahnschrift 12")
            arpPoisonTargetIpLabel.place(x = 10, y = 70)

            self.arpPoisonTargetIpEntry = Entry(arpPoisonFrame, width = 20, font="bahnschrift 12", fg="#ffffff", bg="#252525")
            self.arpPoisonTargetIpEntry.place(x = 300, y = 70)

            arpPoisonDefaultGateLabel = Label(arpPoisonFrame, text="Target Default Gateway         :", fg="#ffffff", bg="#612601", font="bahnschrift 12")
            arpPoisonDefaultGateLabel.place(x = 10, y = 120)

            self.arpPoisonDefaultGateEntry = Entry(arpPoisonFrame, width = 20, font="bahnschrift 12", fg="#ffffff", bg="#252525")
            self.arpPoisonDefaultGateEntry.place(x = 300, y = 120)



            arpPoisonTerminalLabel = Label(arpPoisonFrame, text="Terminal", fg="#ffffff", bg="#612601", font="bahnschrift 15")
            arpPoisonTerminalLabel.place(x = 660, y = 20)

            arpPoisonTerminalFrame = Frame(arpPoisonFrame, width=300, height=120, background="#252525", highlightbackground="#ffffff", highlightthickness=2)
            arpPoisonTerminalFrame.pack_propagate(False)
            arpPoisonTerminalFrame.place(x = 555, y = 55)

            arpPoisonTerminalScrollCanvas = Canvas(arpPoisonTerminalFrame, background="#252525", highlightbackground="#ffffff", yscrollincrement=8)
            arpPoisonTerminalScrollCanvas.pack(side = LEFT, fill = BOTH, expand = 1)
        
            arpPoisonTerminalVerticalScrollbar = Scrollbar(arpPoisonTerminalScrollCanvas, orient=VERTICAL, command = arpPoisonTerminalScrollCanvas.yview)
            arpPoisonTerminalVerticalScrollbar.pack(side = RIGHT, fill = Y)

            arpPoisonTerminalHorizontalScrollbar = Scrollbar(arpPoisonTerminalScrollCanvas, orient=HORIZONTAL, command = arpPoisonTerminalScrollCanvas.xview)
            arpPoisonTerminalHorizontalScrollbar.pack(side = BOTTOM, fill = X)

            arpPoisonTerminalScrollCanvas.configure(yscrollcommand=arpPoisonTerminalVerticalScrollbar.set)
            arpPoisonTerminalScrollCanvas.bind("<Configure>", lambda e : arpPoisonTerminalScrollCanvas.configure(scrollregion=arpPoisonTerminalScrollCanvas.bbox("all")))
            arpPoisonTerminalScrollCanvas.bind_all("<MouseWheel>", lambda e : arpPoisonTerminalScrollCanvas.yview_scroll(-1, "units"))

            arpPoisonTerminalScrollCanvas.configure(xscrollcommand=arpPoisonTerminalHorizontalScrollbar.set)
            arpPoisonTerminalScrollCanvas.bind("<Configure>", lambda e : arpPoisonTerminalScrollCanvas.configure(scrollregion=arpPoisonTerminalScrollCanvas.bbox("all")))
            arpPoisonTerminalScrollCanvas.bind_all("<MouseWheel>", lambda e : arpPoisonTerminalScrollCanvas.xview_scroll(-1, "units"))

            self.arpPoisonTerminalContentFrame = Frame(arpPoisonTerminalScrollCanvas, background="#252525", highlightbackground="#ffffff")
            arpPoisonTerminalScrollCanvas.create_window((0,0), window = self.arpPoisonTerminalContentFrame, anchor = NW)
            self.arpPoisonTerminalContentFrame.bind("<Configure>", lambda e : arpPoisonTerminalScrollCanvas.configure(scrollregion=arpPoisonTerminalScrollCanvas.bbox("all")))



            arpPoisonErrorLabel = Label(arpPoisonFrame, text="Errors", fg="#ffffff", bg="#612601", font="bahnschrift 15")
            arpPoisonErrorLabel.place(x = 1035, y = 20)

            arpPoisonErrorOutputFrame = Frame(arpPoisonFrame, width=300, height=120, background="#252525", highlightbackground="#ffffff", highlightthickness=2)
            arpPoisonErrorOutputFrame.pack_propagate(False)
            arpPoisonErrorOutputFrame.place(x = 915, y = 55)

            arpPoisonErrorOutputScrollCanvas = Canvas(arpPoisonErrorOutputFrame, background="#252525", highlightbackground="#ffffff", yscrollincrement=8)
            arpPoisonErrorOutputScrollCanvas.pack(side = LEFT, fill = BOTH, expand=1)
        
            arpPoisonErrorOutputVerticalScrollbar = Scrollbar(arpPoisonErrorOutputScrollCanvas, orient=VERTICAL, command = arpPoisonErrorOutputScrollCanvas.yview)
            arpPoisonErrorOutputVerticalScrollbar.pack(side = RIGHT, fill = Y)

            arpPoisonErrorOutputHorizontalScrollbar = Scrollbar(arpPoisonErrorOutputScrollCanvas, orient=HORIZONTAL, command = arpPoisonErrorOutputScrollCanvas.xview)
            arpPoisonErrorOutputHorizontalScrollbar.pack(side = BOTTOM, fill = X)

            arpPoisonErrorOutputScrollCanvas.configure(yscrollcommand=arpPoisonErrorOutputVerticalScrollbar.set)
            arpPoisonErrorOutputScrollCanvas.bind("<Configure>", lambda e : arpPoisonErrorOutputScrollCanvas.configure(scrollregion=arpPoisonErrorOutputScrollCanvas.bbox("all")))
            arpPoisonErrorOutputFrame.bind_all("<MouseWheel>", lambda e : arpPoisonErrorOutputScrollCanvas.yview_scroll(-1, "units"))

            arpPoisonErrorOutputScrollCanvas.configure(xscrollcommand=arpPoisonErrorOutputHorizontalScrollbar.set)
            arpPoisonErrorOutputScrollCanvas.bind("<Configure>", lambda e : arpPoisonErrorOutputScrollCanvas.configure(scrollregion=arpPoisonErrorOutputScrollCanvas.bbox("all")))
            arpPoisonErrorOutputFrame.bind_all("<MouseWheel>", lambda e : arpPoisonErrorOutputScrollCanvas.xview_scroll(-1, "units"))

            self.arpPoisonErrorOutputContentFrame = Frame(arpPoisonErrorOutputScrollCanvas, background="#252525", highlightbackground="#ffffff")
            arpPoisonErrorOutputScrollCanvas.create_window((0,0), window = self.arpPoisonErrorOutputContentFrame, anchor = NW)
            self.arpPoisonErrorOutputContentFrame.bind("<Configure>", lambda e : arpPoisonErrorOutputScrollCanvas.configure(scrollregion=arpPoisonErrorOutputScrollCanvas.bbox("all")))
        
        elif chosenAttackType == "MAC Address Spoofing" :
            macAddressSpoofFrame = Frame(self.attacksScrollFrame, width=1280, height=200, background="#612601", borderwidth=3, relief="raised")
            macAddressSpoofFrame.pack()

            macAddressSpoofLabel = Label(macAddressSpoofFrame, text=" MAC Address Spoofing ", fg="#ffffff", bg="#2E1201", font="bahnschrift 12")
            macAddressSpoofLabel.place(x=0, y=0)
            
            macAddressSpoofNoInputLabel = Label(macAddressSpoofFrame, text="No Input Needed", fg="#ffffff", bg="#612601", font="bahnschrift 12")
            macAddressSpoofNoInputLabel.place(x = 10, y = 95)



            macAddressSpoofTerminalLabel = Label(macAddressSpoofFrame, text="Terminal", fg="#ffffff", bg="#612601", font="bahnschrift 15")
            macAddressSpoofTerminalLabel.place(x = 660, y = 20)

            macAddressSpoofTerminalFrame = Frame(macAddressSpoofFrame, width=300, height=120, background="#252525", highlightbackground="#ffffff", highlightthickness=2)
            macAddressSpoofTerminalFrame.pack_propagate(False)
            macAddressSpoofTerminalFrame.place(x = 555, y = 55)

            macAddressSpoofTerminalScrollCanvas = Canvas(macAddressSpoofTerminalFrame, background="#252525", highlightbackground="#ffffff", yscrollincrement=8)
            macAddressSpoofTerminalScrollCanvas.pack(side = LEFT, fill = BOTH, expand = 1)
        
            macAddressSpoofTerminalVerticalScrollbar = Scrollbar(macAddressSpoofTerminalScrollCanvas, orient=VERTICAL, command = macAddressSpoofTerminalScrollCanvas.yview)
            macAddressSpoofTerminalVerticalScrollbar.pack(side = RIGHT, fill = Y)

            macAddressSpoofTerminalHorizontalScrollbar = Scrollbar(macAddressSpoofTerminalScrollCanvas, orient=HORIZONTAL, command = macAddressSpoofTerminalScrollCanvas.xview)
            macAddressSpoofTerminalHorizontalScrollbar.pack(side = BOTTOM, fill = X)

            macAddressSpoofTerminalScrollCanvas.configure(yscrollcommand=macAddressSpoofTerminalVerticalScrollbar.set)
            macAddressSpoofTerminalScrollCanvas.bind("<Configure>", lambda e : macAddressSpoofTerminalScrollCanvas.configure(scrollregion=macAddressSpoofTerminalScrollCanvas.bbox("all")))
            macAddressSpoofTerminalScrollCanvas.bind_all("<MouseWheel>", lambda e : macAddressSpoofTerminalScrollCanvas.yview_scroll(-1, "units"))

            macAddressSpoofTerminalScrollCanvas.configure(xscrollcommand=macAddressSpoofTerminalHorizontalScrollbar.set)
            macAddressSpoofTerminalScrollCanvas.bind("<Configure>", lambda e : macAddressSpoofTerminalScrollCanvas.configure(scrollregion=macAddressSpoofTerminalScrollCanvas.bbox("all")))
            macAddressSpoofTerminalScrollCanvas.bind_all("<MouseWheel>", lambda e : macAddressSpoofTerminalScrollCanvas.xview_scroll(-1, "units"))

            self.macAddressSpoofTerminalContentFrame = Frame(macAddressSpoofTerminalScrollCanvas, background="#252525", highlightbackground="#ffffff")
            macAddressSpoofTerminalScrollCanvas.create_window((0,0), window = self.macAddressSpoofTerminalContentFrame, anchor = NW)
            self.macAddressSpoofTerminalContentFrame.bind("<Configure>", lambda e : macAddressSpoofTerminalScrollCanvas.configure(scrollregion=macAddressSpoofTerminalScrollCanvas.bbox("all")))



            macAddressSpoofErrorLabel = Label(macAddressSpoofFrame, text="Errors", fg="#ffffff", bg="#612601", font="bahnschrift 15")
            macAddressSpoofErrorLabel.place(x = 1035, y = 20)

            macAddressSpoofErrorOutputFrame = Frame(macAddressSpoofFrame, width=300, height=120, background="#252525", highlightbackground="#ffffff", highlightthickness=2)
            macAddressSpoofErrorOutputFrame.pack_propagate(False)
            macAddressSpoofErrorOutputFrame.place(x = 915, y = 55)

            macAddressSpoofErrorOutputScrollCanvas = Canvas(macAddressSpoofErrorOutputFrame, background="#252525", highlightbackground="#ffffff", yscrollincrement=8)
            macAddressSpoofErrorOutputScrollCanvas.pack(side = LEFT, fill = BOTH, expand=1)
        
            macAddressSpoofErrorOutputVerticalScrollbar = Scrollbar(macAddressSpoofErrorOutputScrollCanvas, orient=VERTICAL, command = macAddressSpoofErrorOutputScrollCanvas.yview)
            macAddressSpoofErrorOutputVerticalScrollbar.pack(side = RIGHT, fill = Y)

            macAddressSpoofErrorOutputHorizontalScrollbar = Scrollbar(macAddressSpoofErrorOutputScrollCanvas, orient=HORIZONTAL, command = macAddressSpoofErrorOutputScrollCanvas.xview)
            macAddressSpoofErrorOutputHorizontalScrollbar.pack(side = BOTTOM, fill = X)

            macAddressSpoofErrorOutputScrollCanvas.configure(yscrollcommand=macAddressSpoofErrorOutputVerticalScrollbar.set)
            macAddressSpoofErrorOutputScrollCanvas.bind("<Configure>", lambda e : macAddressSpoofErrorOutputScrollCanvas.configure(scrollregion=macAddressSpoofErrorOutputScrollCanvas.bbox("all")))
            macAddressSpoofErrorOutputFrame.bind_all("<MouseWheel>", lambda e : macAddressSpoofErrorOutputScrollCanvas.yview_scroll(-1, "units"))

            macAddressSpoofErrorOutputScrollCanvas.configure(xscrollcommand=macAddressSpoofErrorOutputHorizontalScrollbar.set)
            macAddressSpoofErrorOutputScrollCanvas.bind("<Configure>", lambda e : macAddressSpoofErrorOutputScrollCanvas.configure(scrollregion=macAddressSpoofErrorOutputScrollCanvas.bbox("all")))
            macAddressSpoofErrorOutputFrame.bind_all("<MouseWheel>", lambda e : macAddressSpoofErrorOutputScrollCanvas.xview_scroll(-1, "units"))

            self.macAddressSpoofErrorOutputContentFrame = Frame(macAddressSpoofErrorOutputScrollCanvas, background="#252525", highlightbackground="#ffffff")
            macAddressSpoofErrorOutputScrollCanvas.create_window((0,0), window = self.macAddressSpoofErrorOutputContentFrame, anchor = NW)
            self.macAddressSpoofErrorOutputContentFrame.bind("<Configure>", lambda e : macAddressSpoofErrorOutputScrollCanvas.configure(scrollregion=macAddressSpoofErrorOutputScrollCanvas.bbox("all")))
        
        elif chosenAttackType == "Syn Flooding" :
            synFloodFrame = Frame(self.attacksScrollFrame, width=1280, height=200, background="#612601", borderwidth=3, relief="raised")
            synFloodFrame.pack()

            synFloodLabel = Label(synFloodFrame, text=" Syn Flooding Attack ", fg="#ffffff", bg="#2E1201", font="bahnschrift 12")
            synFloodLabel.place(x=0, y=0)

            synFloodTargetIpLabel = Label(synFloodFrame, text="Target IP Address              :", fg="#ffffff", bg="#612601", font="bahnschrift 12")
            synFloodTargetIpLabel.place(x = 10, y = 70)

            self.synFloodTargetIpEntry = Entry(synFloodFrame, width = 20, font="bahnschrift 12", fg="#ffffff", bg="#252525")
            self.synFloodTargetIpEntry.place(x = 300, y = 70)

            synFloodPortLabel = Label(synFloodFrame, text="Target Port                        :", fg="#ffffff", bg="#612601", font="bahnschrift 12")
            synFloodPortLabel.place(x = 10, y = 120)

            self.synFloodPortEntry = Entry(synFloodFrame, width = 20, font="bahnschrift 12", fg="#ffffff", bg="#252525")
            self.synFloodPortEntry.place(x = 300, y = 120)



            synFloodTerminalLabel = Label(synFloodFrame, text="Terminal", fg="#ffffff", bg="#612601", font="bahnschrift 15")
            synFloodTerminalLabel.place(x = 660, y = 20)

            synFloodTerminalFrame = Frame(synFloodFrame, width=300, height=120, background="#252525", highlightbackground="#ffffff", highlightthickness=2)
            synFloodTerminalFrame.pack_propagate(False)
            synFloodTerminalFrame.place(x = 555, y = 55)

            synFloodTerminalScrollCanvas = Canvas(synFloodTerminalFrame, background="#252525", highlightbackground="#ffffff", yscrollincrement=8)
            synFloodTerminalScrollCanvas.pack(side = LEFT, fill = BOTH, expand = 1)
        
            synFloodTerminalVerticalScrollbar = Scrollbar(synFloodTerminalScrollCanvas, orient=VERTICAL, command = synFloodTerminalScrollCanvas.yview)
            synFloodTerminalVerticalScrollbar.pack(side = RIGHT, fill = Y)

            synFloodTerminalHorizontalScrollbar = Scrollbar(synFloodTerminalScrollCanvas, orient=HORIZONTAL, command = synFloodTerminalScrollCanvas.xview)
            synFloodTerminalHorizontalScrollbar.pack(side = BOTTOM, fill = X)

            synFloodTerminalScrollCanvas.configure(yscrollcommand=synFloodTerminalVerticalScrollbar.set)
            synFloodTerminalScrollCanvas.bind("<Configure>", lambda e : synFloodTerminalScrollCanvas.configure(scrollregion=synFloodTerminalScrollCanvas.bbox("all")))
            synFloodTerminalScrollCanvas.bind_all("<MouseWheel>", lambda e : synFloodTerminalScrollCanvas.yview_scroll(-1, "units"))

            synFloodTerminalScrollCanvas.configure(xscrollcommand=synFloodTerminalHorizontalScrollbar.set)
            synFloodTerminalScrollCanvas.bind("<Configure>", lambda e : synFloodTerminalScrollCanvas.configure(scrollregion=synFloodTerminalScrollCanvas.bbox("all")))
            synFloodTerminalScrollCanvas.bind_all("<MouseWheel>", lambda e : synFloodTerminalScrollCanvas.xview_scroll(-1, "units"))

            self.synFloodTerminalContentFrame = Frame(synFloodTerminalScrollCanvas, background="#252525", highlightbackground="#ffffff")
            synFloodTerminalScrollCanvas.create_window((0,0), window = self.synFloodTerminalContentFrame, anchor = NW)
            self.synFloodTerminalContentFrame.bind("<Configure>", lambda e : synFloodTerminalScrollCanvas.configure(scrollregion=synFloodTerminalScrollCanvas.bbox("all")))



            synFloodErrorLabel = Label(synFloodFrame, text="Errors", fg="#ffffff", bg="#612601", font="bahnschrift 15")
            synFloodErrorLabel.place(x = 1035, y = 20)

            synFloodErrorOutputFrame = Frame(synFloodFrame, width=300, height=120, background="#252525", highlightbackground="#ffffff", highlightthickness=2)
            synFloodErrorOutputFrame.pack_propagate(False)
            synFloodErrorOutputFrame.place(x = 915, y = 55)

            synFloodErrorOutputScrollCanvas = Canvas(synFloodErrorOutputFrame, background="#252525", highlightbackground="#ffffff", yscrollincrement=8)
            synFloodErrorOutputScrollCanvas.pack(side = LEFT, fill = BOTH, expand=1)
        
            synFloodErrorOutputVerticalScrollbar = Scrollbar(synFloodErrorOutputScrollCanvas, orient=VERTICAL, command = synFloodErrorOutputScrollCanvas.yview)
            synFloodErrorOutputVerticalScrollbar.pack(side = RIGHT, fill = Y)

            synFloodErrorOutputHorizontalScrollbar = Scrollbar(synFloodErrorOutputScrollCanvas, orient=HORIZONTAL, command = synFloodErrorOutputScrollCanvas.xview)
            synFloodErrorOutputHorizontalScrollbar.pack(side = BOTTOM, fill = X)

            synFloodErrorOutputScrollCanvas.configure(yscrollcommand=synFloodErrorOutputVerticalScrollbar.set)
            synFloodErrorOutputScrollCanvas.bind("<Configure>", lambda e : synFloodErrorOutputScrollCanvas.configure(scrollregion=synFloodErrorOutputScrollCanvas.bbox("all")))
            synFloodErrorOutputFrame.bind_all("<MouseWheel>", lambda e : synFloodErrorOutputScrollCanvas.yview_scroll(-1, "units"))

            synFloodErrorOutputScrollCanvas.configure(xscrollcommand=synFloodErrorOutputHorizontalScrollbar.set)
            synFloodErrorOutputScrollCanvas.bind("<Configure>", lambda e : synFloodErrorOutputScrollCanvas.configure(scrollregion=synFloodErrorOutputScrollCanvas.bbox("all")))
            synFloodErrorOutputFrame.bind_all("<MouseWheel>", lambda e : synFloodErrorOutputScrollCanvas.xview_scroll(-1, "units"))

            self.synFloodErrorOutputContentFrame = Frame(synFloodErrorOutputScrollCanvas, background="#252525", highlightbackground="#ffffff")
            synFloodErrorOutputScrollCanvas.create_window((0,0), window = self.synFloodErrorOutputContentFrame, anchor = NW)
            self.synFloodErrorOutputContentFrame.bind("<Configure>", lambda e : synFloodErrorOutputScrollCanvas.configure(scrollregion=synFloodErrorOutputScrollCanvas.bbox("all")))

        elif chosenAttackType == "ICMP Attack" :
            icmpAttackFrame = Frame(self.attacksScrollFrame, width=1280, height=200, background="#612601", borderwidth=3, relief="raised")
            icmpAttackFrame.pack()

            icmpAttackLabel = Label(icmpAttackFrame, text=" ICMP Attack ", fg="#ffffff", bg="#2E1201", font="bahnschrift 12")
            icmpAttackLabel.place(x=0, y=0)

            icmpAttackTargetIpLabel = Label(icmpAttackFrame, text="Target IP Address              :", fg="#ffffff", bg="#612601", font="bahnschrift 12")
            icmpAttackTargetIpLabel.place(x = 10, y = 95)

            self.icmpAttackTargetIpEntry = Entry(icmpAttackFrame, width = 20, font="bahnschrift 12", fg="#ffffff", bg="#252525")
            self.icmpAttackTargetIpEntry.place(x = 300, y = 95)



            icmpAttackTerminalLabel = Label(icmpAttackFrame, text="Terminal", fg="#ffffff", bg="#612601", font="bahnschrift 15")
            icmpAttackTerminalLabel.place(x = 660, y = 20)

            icmpAttackTerminalFrame = Frame(icmpAttackFrame, width=300, height=120, background="#252525", highlightbackground="#ffffff", highlightthickness=2)
            icmpAttackTerminalFrame.pack_propagate(False)
            icmpAttackTerminalFrame.place(x = 555, y = 55)

            icmpAttackTerminalScrollCanvas = Canvas(icmpAttackTerminalFrame, background="#252525", highlightbackground="#ffffff", yscrollincrement=8)
            icmpAttackTerminalScrollCanvas.pack(side = LEFT, fill = BOTH, expand = 1)
        
            icmpAttackTerminalVerticalScrollbar = Scrollbar(icmpAttackTerminalScrollCanvas, orient=VERTICAL, command = icmpAttackTerminalScrollCanvas.yview)
            icmpAttackTerminalVerticalScrollbar.pack(side = RIGHT, fill = Y)

            icmpAttackTerminalHorizontalScrollbar = Scrollbar(icmpAttackTerminalScrollCanvas, orient=HORIZONTAL, command = icmpAttackTerminalScrollCanvas.xview)
            icmpAttackTerminalHorizontalScrollbar.pack(side = BOTTOM, fill = X)

            icmpAttackTerminalScrollCanvas.configure(yscrollcommand=icmpAttackTerminalVerticalScrollbar.set)
            icmpAttackTerminalScrollCanvas.bind("<Configure>", lambda e : icmpAttackTerminalScrollCanvas.configure(scrollregion=icmpAttackTerminalScrollCanvas.bbox("all")))
            icmpAttackTerminalScrollCanvas.bind_all("<MouseWheel>", lambda e : icmpAttackTerminalScrollCanvas.yview_scroll(-1, "units"))

            icmpAttackTerminalScrollCanvas.configure(xscrollcommand=icmpAttackTerminalHorizontalScrollbar.set)
            icmpAttackTerminalScrollCanvas.bind("<Configure>", lambda e : icmpAttackTerminalScrollCanvas.configure(scrollregion=icmpAttackTerminalScrollCanvas.bbox("all")))
            icmpAttackTerminalScrollCanvas.bind_all("<MouseWheel>", lambda e : icmpAttackTerminalScrollCanvas.xview_scroll(-1, "units"))

            self.icmpAttackTerminalContentFrame = Frame(icmpAttackTerminalScrollCanvas, background="#252525", highlightbackground="#ffffff")
            icmpAttackTerminalScrollCanvas.create_window((0,0), window = self.icmpAttackTerminalContentFrame, anchor = NW)
            self.icmpAttackTerminalContentFrame.bind("<Configure>", lambda e : icmpAttackTerminalScrollCanvas.configure(scrollregion=icmpAttackTerminalScrollCanvas.bbox("all")))



            icmpAttackErrorLabel = Label(icmpAttackFrame, text="Errors", fg="#ffffff", bg="#612601", font="bahnschrift 15")
            icmpAttackErrorLabel.place(x = 1035, y = 20)

            icmpAttackErrorOutputFrame = Frame(icmpAttackFrame, width=300, height=120, background="#252525", highlightbackground="#ffffff", highlightthickness=2)
            icmpAttackErrorOutputFrame.pack_propagate(False)
            icmpAttackErrorOutputFrame.place(x = 915, y = 55)

            icmpAttackErrorOutputScrollCanvas = Canvas(icmpAttackErrorOutputFrame, background="#252525", highlightbackground="#ffffff", yscrollincrement=8)
            icmpAttackErrorOutputScrollCanvas.pack(side = LEFT, fill = BOTH, expand=1)
        
            icmpAttackErrorOutputVerticalScrollbar = Scrollbar(icmpAttackErrorOutputScrollCanvas, orient=VERTICAL, command = icmpAttackErrorOutputScrollCanvas.yview)
            icmpAttackErrorOutputVerticalScrollbar.pack(side = RIGHT, fill = Y)

            icmpAttackErrorOutputHorizontalScrollbar = Scrollbar(icmpAttackErrorOutputScrollCanvas, orient=HORIZONTAL, command = icmpAttackErrorOutputScrollCanvas.xview)
            icmpAttackErrorOutputHorizontalScrollbar.pack(side = BOTTOM, fill = X)

            icmpAttackErrorOutputScrollCanvas.configure(yscrollcommand=icmpAttackErrorOutputVerticalScrollbar.set)
            icmpAttackErrorOutputScrollCanvas.bind("<Configure>", lambda e : icmpAttackErrorOutputScrollCanvas.configure(scrollregion=icmpAttackErrorOutputScrollCanvas.bbox("all")))
            icmpAttackErrorOutputFrame.bind_all("<MouseWheel>", lambda e : icmpAttackErrorOutputScrollCanvas.yview_scroll(-1, "units"))

            icmpAttackErrorOutputScrollCanvas.configure(xscrollcommand=icmpAttackErrorOutputHorizontalScrollbar.set)
            icmpAttackErrorOutputScrollCanvas.bind("<Configure>", lambda e : icmpAttackErrorOutputScrollCanvas.configure(scrollregion=icmpAttackErrorOutputScrollCanvas.bbox("all")))
            icmpAttackErrorOutputFrame.bind_all("<MouseWheel>", lambda e : icmpAttackErrorOutputScrollCanvas.xview_scroll(-1, "units"))

            self.icmpAttackErrorOutputContentFrame = Frame(icmpAttackErrorOutputScrollCanvas, background="#252525", highlightbackground="#ffffff")
            icmpAttackErrorOutputScrollCanvas.create_window((0,0), window = self.icmpAttackErrorOutputContentFrame, anchor = NW)
            self.icmpAttackErrorOutputContentFrame.bind("<Configure>", lambda e : icmpAttackErrorOutputScrollCanvas.configure(scrollregion=icmpAttackErrorOutputScrollCanvas.bbox("all")))

        elif chosenAttackType == "DNS Amplification" :
            dnsAmpFrame = Frame(self.attacksScrollFrame, width=1280, height=200, background="#612601", borderwidth=3, relief="raised")
            dnsAmpFrame.pack()

            dnsAmpLabel = Label(dnsAmpFrame, text=" DNS Amplification ", fg="#ffffff", bg="#2E1201", font="bahnschrift 12")
            dnsAmpLabel.place(x=0, y=0)

            dnsAmpTargetIpLabel = Label(dnsAmpFrame, text="Target IP Address                   :", fg="#ffffff", bg="#612601", font="bahnschrift 12")
            dnsAmpTargetIpLabel.place(x = 10, y = 70)

            self.dnsAmpTargetIpEntry = Entry(dnsAmpFrame, width = 20, font="bahnschrift 12", fg="#ffffff", bg="#252525")
            self.dnsAmpTargetIpEntry.place(x = 300, y = 70)

            dnsAmpPacketLabel = Label(dnsAmpFrame, text="DNS Packet Amount (Int)        :", fg="#ffffff", bg="#612601", font="bahnschrift 12")
            dnsAmpPacketLabel.place(x = 10, y = 120)

            self.dnsAmpPacketEntry = Entry(dnsAmpFrame, width = 20, font="bahnschrift 12", fg="#ffffff", bg="#252525")
            self.dnsAmpPacketEntry.place(x = 300, y = 120)



            dnsAmpTerminalLabel = Label(dnsAmpFrame, text="Terminal", fg="#ffffff", bg="#612601", font="bahnschrift 15")
            dnsAmpTerminalLabel.place(x = 660, y = 20)

            dnsAmpTerminalFrame = Frame(dnsAmpFrame, width=300, height=120, background="#252525", highlightbackground="#ffffff", highlightthickness=2)
            dnsAmpTerminalFrame.pack_propagate(False)
            dnsAmpTerminalFrame.place(x = 555, y = 55)

            dnsAmpTerminalScrollCanvas = Canvas(dnsAmpTerminalFrame, background="#252525", highlightbackground="#ffffff", yscrollincrement=8)
            dnsAmpTerminalScrollCanvas.pack(side = LEFT, fill = BOTH, expand = 1)
        
            dnsAmpTerminalVerticalScrollbar = Scrollbar(dnsAmpTerminalScrollCanvas, orient=VERTICAL, command = dnsAmpTerminalScrollCanvas.yview)
            dnsAmpTerminalVerticalScrollbar.pack(side = RIGHT, fill = Y)

            dnsAmpTerminalHorizontalScrollbar = Scrollbar(dnsAmpTerminalScrollCanvas, orient=HORIZONTAL, command = dnsAmpTerminalScrollCanvas.xview)
            dnsAmpTerminalHorizontalScrollbar.pack(side = BOTTOM, fill = X)

            dnsAmpTerminalScrollCanvas.configure(yscrollcommand=dnsAmpTerminalVerticalScrollbar.set)
            dnsAmpTerminalScrollCanvas.bind("<Configure>", lambda e : dnsAmpTerminalScrollCanvas.configure(scrollregion=dnsAmpTerminalScrollCanvas.bbox("all")))
            dnsAmpTerminalScrollCanvas.bind_all("<MouseWheel>", lambda e : dnsAmpTerminalScrollCanvas.yview_scroll(-1, "units"))

            dnsAmpTerminalScrollCanvas.configure(xscrollcommand=dnsAmpTerminalHorizontalScrollbar.set)
            dnsAmpTerminalScrollCanvas.bind("<Configure>", lambda e : dnsAmpTerminalScrollCanvas.configure(scrollregion=dnsAmpTerminalScrollCanvas.bbox("all")))
            dnsAmpTerminalScrollCanvas.bind_all("<MouseWheel>", lambda e : dnsAmpTerminalScrollCanvas.xview_scroll(-1, "units"))

            self.dnsAmpTerminalContentFrame = Frame(dnsAmpTerminalScrollCanvas, background="#252525", highlightbackground="#ffffff")
            dnsAmpTerminalScrollCanvas.create_window((0,0), window = self.dnsAmpTerminalContentFrame, anchor = NW)
            self.dnsAmpTerminalContentFrame.bind("<Configure>", lambda e : dnsAmpTerminalScrollCanvas.configure(scrollregion=dnsAmpTerminalScrollCanvas.bbox("all")))



            dnsAmpErrorLabel = Label(dnsAmpFrame, text="Errors", fg="#ffffff", bg="#612601", font="bahnschrift 15")
            dnsAmpErrorLabel.place(x = 1035, y = 20)

            dnsAmpErrorOutputFrame = Frame(dnsAmpFrame, width=300, height=120, background="#252525", highlightbackground="#ffffff", highlightthickness=2)
            dnsAmpErrorOutputFrame.pack_propagate(False)
            dnsAmpErrorOutputFrame.place(x = 915, y = 55)

            dnsAmpErrorOutputScrollCanvas = Canvas(dnsAmpErrorOutputFrame, background="#252525", highlightbackground="#ffffff", yscrollincrement=8)
            dnsAmpErrorOutputScrollCanvas.pack(side = LEFT, fill = BOTH, expand=1)
        
            dnsAmpErrorOutputVerticalScrollbar = Scrollbar(dnsAmpErrorOutputScrollCanvas, orient=VERTICAL, command = dnsAmpErrorOutputScrollCanvas.yview)
            dnsAmpErrorOutputVerticalScrollbar.pack(side = RIGHT, fill = Y)

            dnsAmpErrorOutputHorizontalScrollbar = Scrollbar(dnsAmpErrorOutputScrollCanvas, orient=HORIZONTAL, command = dnsAmpErrorOutputScrollCanvas.xview)
            dnsAmpErrorOutputHorizontalScrollbar.pack(side = BOTTOM, fill = X)

            dnsAmpErrorOutputScrollCanvas.configure(yscrollcommand=dnsAmpErrorOutputVerticalScrollbar.set)
            dnsAmpErrorOutputScrollCanvas.bind("<Configure>", lambda e : dnsAmpErrorOutputScrollCanvas.configure(scrollregion=dnsAmpErrorOutputScrollCanvas.bbox("all")))
            dnsAmpErrorOutputFrame.bind_all("<MouseWheel>", lambda e : dnsAmpErrorOutputScrollCanvas.yview_scroll(-1, "units"))

            dnsAmpErrorOutputScrollCanvas.configure(xscrollcommand=dnsAmpErrorOutputHorizontalScrollbar.set)
            dnsAmpErrorOutputScrollCanvas.bind("<Configure>", lambda e : dnsAmpErrorOutputScrollCanvas.configure(scrollregion=dnsAmpErrorOutputScrollCanvas.bbox("all")))
            dnsAmpErrorOutputFrame.bind_all("<MouseWheel>", lambda e : dnsAmpErrorOutputScrollCanvas.xview_scroll(-1, "units"))

            self.dnsAmpErrorOutputContentFrame = Frame(dnsAmpErrorOutputScrollCanvas, background="#252525", highlightbackground="#ffffff")
            dnsAmpErrorOutputScrollCanvas.create_window((0,0), window = self.dnsAmpErrorOutputContentFrame, anchor = NW)
            self.dnsAmpErrorOutputContentFrame.bind("<Configure>", lambda e : dnsAmpErrorOutputScrollCanvas.configure(scrollregion=dnsAmpErrorOutputScrollCanvas.bbox("all")))
        
        elif chosenAttackType == "DNS Spoofing" :
            dnsSpoofFrame = Frame(self.attacksScrollFrame, width=1280, height=200, background="#612601", borderwidth=3, relief="raised")
            dnsSpoofFrame.pack()

            dnsSpoofLabel = Label(dnsSpoofFrame, text=" DNS Spoofing ", fg="#ffffff", bg="#2E1201", font="bahnschrift 12")
            dnsSpoofLabel.place(x=0, y=0)

            dnsSpoofInterfaceLabel = Label(dnsSpoofFrame, text="Interface                          :", fg="#ffffff", bg="#612601", font="bahnschrift 12")
            dnsSpoofInterfaceLabel.place(x = 10, y = 48)

            self.dnsSpoofInterfaceEntry = Entry(dnsSpoofFrame, width = 20, font="bahnschrift 12", fg="#ffffff", bg="#252525")
            self.dnsSpoofInterfaceEntry.place(x = 300, y = 48)

            dnsSpoofTargetIpLabel = Label(dnsSpoofFrame, text="Target IP                          :", fg="#ffffff", bg="#612601", font="bahnschrift 12")
            dnsSpoofTargetIpLabel.place(x = 10, y = 98)

            self.dnsSpoofTargetIpEntry = Entry(dnsSpoofFrame, width = 20, font="bahnschrift 12", fg="#ffffff", bg="#252525")
            self.dnsSpoofTargetIpEntry.place(x = 300, y = 98)

            dnsSpoofTargetDomainsLabel = Label(dnsSpoofFrame, text="Target Domains               :", fg="#ffffff", bg="#612601", font="bahnschrift 12")
            dnsSpoofTargetDomainsLabel.place(x = 10, y = 148)

            self.dnsSpoofTargetDomainsEntry = Entry(dnsSpoofFrame, width = 20, font="bahnschrift 12", fg="#ffffff", bg="#252525")
            self.dnsSpoofTargetDomainsEntry.insert(0, "Seperate Domains by \",\"")
            self.dnsSpoofTargetDomainsEntry.bind("<Button-1>", lambda e : self.dnsSpoofTargetDomainsEntry.delete(0,"end"))
            self.dnsSpoofTargetDomainsEntry.place(x = 300, y = 148)



            dnsSpoofTerminalLabel = Label(dnsSpoofFrame, text="Terminal", fg="#ffffff", bg="#612601", font="bahnschrift 15")
            dnsSpoofTerminalLabel.place(x = 660, y = 20)

            dnsSpoofTerminalFrame = Frame(dnsSpoofFrame, width=300, height=120, background="#252525", highlightbackground="#ffffff", highlightthickness=2)
            dnsSpoofTerminalFrame.pack_propagate(False)
            dnsSpoofTerminalFrame.place(x = 555, y = 55)

            dnsSpoofTerminalScrollCanvas = Canvas(dnsSpoofTerminalFrame, background="#252525", highlightbackground="#ffffff", yscrollincrement=8)
            dnsSpoofTerminalScrollCanvas.pack(side = LEFT, fill = BOTH, expand = 1)
        
            dnsSpoofTerminalVerticalScrollbar = Scrollbar(dnsSpoofTerminalScrollCanvas, orient=VERTICAL, command = dnsSpoofTerminalScrollCanvas.yview)
            dnsSpoofTerminalVerticalScrollbar.pack(side = RIGHT, fill = Y)

            dnsSpoofTerminalHorizontalScrollbar = Scrollbar(dnsSpoofTerminalScrollCanvas, orient=HORIZONTAL, command = dnsSpoofTerminalScrollCanvas.xview)
            dnsSpoofTerminalHorizontalScrollbar.pack(side = BOTTOM, fill = X)

            dnsSpoofTerminalScrollCanvas.configure(yscrollcommand=dnsSpoofTerminalVerticalScrollbar.set)
            dnsSpoofTerminalScrollCanvas.bind("<Configure>", lambda e : dnsSpoofTerminalScrollCanvas.configure(scrollregion=dnsSpoofTerminalScrollCanvas.bbox("all")))
            dnsSpoofTerminalScrollCanvas.bind_all("<MouseWheel>", lambda e : dnsSpoofTerminalScrollCanvas.yview_scroll(-1, "units"))

            dnsSpoofTerminalScrollCanvas.configure(xscrollcommand=dnsSpoofTerminalHorizontalScrollbar.set)
            dnsSpoofTerminalScrollCanvas.bind("<Configure>", lambda e : dnsSpoofTerminalScrollCanvas.configure(scrollregion=dnsSpoofTerminalScrollCanvas.bbox("all")))
            dnsSpoofTerminalScrollCanvas.bind_all("<MouseWheel>", lambda e : dnsSpoofTerminalScrollCanvas.xview_scroll(-1, "units"))

            self.dnsSpoofTerminalContentFrame = Frame(dnsSpoofTerminalScrollCanvas, background="#252525", highlightbackground="#ffffff")
            dnsSpoofTerminalScrollCanvas.create_window((0,0), window = self.dnsSpoofTerminalContentFrame, anchor = NW)
            self.dnsSpoofTerminalContentFrame.bind("<Configure>", lambda e : dnsSpoofTerminalScrollCanvas.configure(scrollregion=dnsSpoofTerminalScrollCanvas.bbox("all")))



            dnsSpoofErrorLabel = Label(dnsSpoofFrame, text="Errors", fg="#ffffff", bg="#612601", font="bahnschrift 15")
            dnsSpoofErrorLabel.place(x = 1035, y = 20)

            dnsSpoofErrorOutputFrame = Frame(dnsSpoofFrame, width=300, height=120, background="#252525", highlightbackground="#ffffff", highlightthickness=2)
            dnsSpoofErrorOutputFrame.pack_propagate(False)
            dnsSpoofErrorOutputFrame.place(x = 915, y = 55)

            dnsSpoofErrorOutputScrollCanvas = Canvas(dnsSpoofErrorOutputFrame, background="#252525", highlightbackground="#ffffff", yscrollincrement=8)
            dnsSpoofErrorOutputScrollCanvas.pack(side = LEFT, fill = BOTH, expand=1)
        
            dnsSpoofErrorOutputVerticalScrollbar = Scrollbar(dnsSpoofErrorOutputScrollCanvas, orient=VERTICAL, command = dnsSpoofErrorOutputScrollCanvas.yview)
            dnsSpoofErrorOutputVerticalScrollbar.pack(side = RIGHT, fill = Y)

            dnsSpoofErrorOutputHorizontalScrollbar = Scrollbar(dnsSpoofErrorOutputScrollCanvas, orient=HORIZONTAL, command = dnsSpoofErrorOutputScrollCanvas.xview)
            dnsSpoofErrorOutputHorizontalScrollbar.pack(side = BOTTOM, fill = X)

            dnsSpoofErrorOutputScrollCanvas.configure(yscrollcommand=dnsSpoofErrorOutputVerticalScrollbar.set)
            dnsSpoofErrorOutputScrollCanvas.bind("<Configure>", lambda e : dnsSpoofErrorOutputScrollCanvas.configure(scrollregion=dnsSpoofErrorOutputScrollCanvas.bbox("all")))
            dnsSpoofErrorOutputFrame.bind_all("<MouseWheel>", lambda e : dnsSpoofErrorOutputScrollCanvas.yview_scroll(-1, "units"))

            dnsSpoofErrorOutputScrollCanvas.configure(xscrollcommand=dnsSpoofErrorOutputHorizontalScrollbar.set)
            dnsSpoofErrorOutputScrollCanvas.bind("<Configure>", lambda e : dnsSpoofErrorOutputScrollCanvas.configure(scrollregion=dnsSpoofErrorOutputScrollCanvas.bbox("all")))
            dnsSpoofErrorOutputFrame.bind_all("<MouseWheel>", lambda e : dnsSpoofErrorOutputScrollCanvas.xview_scroll(-1, "units"))

            self.dnsSpoofErrorOutputContentFrame = Frame(dnsSpoofErrorOutputScrollCanvas, background="#252525", highlightbackground="#ffffff")
            dnsSpoofErrorOutputScrollCanvas.create_window((0,0), window = self.dnsSpoofErrorOutputContentFrame, anchor = NW)
            self.dnsSpoofErrorOutputContentFrame.bind("<Configure>", lambda e : dnsSpoofErrorOutputScrollCanvas.configure(scrollregion=dnsSpoofErrorOutputScrollCanvas.bbox("all")))

        elif chosenAttackType == "HTTP-Man-In-The-Middle" :
            httpMitmFrame = Frame(self.attacksScrollFrame, width=1280, height=200, background="#612601", borderwidth=3, relief="raised")
            httpMitmFrame.pack()

            httpMitmLabel = Label(httpMitmFrame, text=" HTTP Man-In-The-Middle ", fg="#ffffff", bg="#2E1201", font="bahnschrift 12")
            httpMitmLabel.place(x=0, y=0)

            httpMitmInterfaceLabel = Label(httpMitmFrame, text="Interface                    :", fg="#ffffff", bg="#612601", font="bahnschrift 12")
            httpMitmInterfaceLabel.place(x = 10, y = 95)

            self.httpMitmInterfaceEntry = Entry(httpMitmFrame, width = 20, font="bahnschrift 12", fg="#ffffff", bg="#252525")
            self.httpMitmInterfaceEntry.place(x = 300, y = 95)



            httpMitmTerminalLabel = Label(httpMitmFrame, text="Terminal", fg="#ffffff", bg="#612601", font="bahnschrift 15")
            httpMitmTerminalLabel.place(x = 660, y = 20)

            httpMitmTerminalFrame = Frame(httpMitmFrame, width=300, height=120, background="#252525", highlightbackground="#ffffff", highlightthickness=2)
            httpMitmTerminalFrame.pack_propagate(False)
            httpMitmTerminalFrame.place(x = 555, y = 55)

            httpMitmTerminalScrollCanvas = Canvas(httpMitmTerminalFrame, background="#252525", highlightbackground="#ffffff", yscrollincrement=8)
            httpMitmTerminalScrollCanvas.pack(side = LEFT, fill = BOTH, expand = 1)
        
            httpMitmTerminalVerticalScrollbar = Scrollbar(httpMitmTerminalScrollCanvas, orient=VERTICAL, command = httpMitmTerminalScrollCanvas.yview)
            httpMitmTerminalVerticalScrollbar.pack(side = RIGHT, fill = Y)

            httpMitmTerminalHorizontalScrollbar = Scrollbar(httpMitmTerminalScrollCanvas, orient=HORIZONTAL, command = httpMitmTerminalScrollCanvas.xview)
            httpMitmTerminalHorizontalScrollbar.pack(side = BOTTOM, fill = X)

            httpMitmTerminalScrollCanvas.configure(yscrollcommand=httpMitmTerminalVerticalScrollbar.set)
            httpMitmTerminalScrollCanvas.bind("<Configure>", lambda e : httpMitmTerminalScrollCanvas.configure(scrollregion=httpMitmTerminalScrollCanvas.bbox("all")))
            httpMitmTerminalScrollCanvas.bind_all("<MouseWheel>", lambda e : httpMitmTerminalScrollCanvas.yview_scroll(-1, "units"))

            httpMitmTerminalScrollCanvas.configure(xscrollcommand=httpMitmTerminalHorizontalScrollbar.set)
            httpMitmTerminalScrollCanvas.bind("<Configure>", lambda e : httpMitmTerminalScrollCanvas.configure(scrollregion=httpMitmTerminalScrollCanvas.bbox("all")))
            httpMitmTerminalScrollCanvas.bind_all("<MouseWheel>", lambda e : httpMitmTerminalScrollCanvas.xview_scroll(-1, "units"))

            self.httpMitmTerminalContentFrame = Frame(httpMitmTerminalScrollCanvas, background="#252525", highlightbackground="#ffffff")
            httpMitmTerminalScrollCanvas.create_window((0,0), window = self.httpMitmTerminalContentFrame, anchor = NW)
            self.httpMitmTerminalContentFrame.bind("<Configure>", lambda e : httpMitmTerminalScrollCanvas.configure(scrollregion=httpMitmTerminalScrollCanvas.bbox("all")))



            httpMitmErrorLabel = Label(httpMitmFrame, text="Errors", fg="#ffffff", bg="#612601", font="bahnschrift 15")
            httpMitmErrorLabel.place(x = 1035, y = 20)

            httpMitmErrorOutputFrame = Frame(httpMitmFrame, width=300, height=120, background="#252525", highlightbackground="#ffffff", highlightthickness=2)
            httpMitmErrorOutputFrame.pack_propagate(False)
            httpMitmErrorOutputFrame.place(x = 915, y = 55)

            httpMitmErrorOutputScrollCanvas = Canvas(httpMitmErrorOutputFrame, background="#252525", highlightbackground="#ffffff", yscrollincrement=8)
            httpMitmErrorOutputScrollCanvas.pack(side = LEFT, fill = BOTH, expand=1)
        
            httpMitmErrorOutputVerticalScrollbar = Scrollbar(httpMitmErrorOutputScrollCanvas, orient=VERTICAL, command = httpMitmErrorOutputScrollCanvas.yview)
            httpMitmErrorOutputVerticalScrollbar.pack(side = RIGHT, fill = Y)

            httpMitmErrorOutputHorizontalScrollbar = Scrollbar(httpMitmErrorOutputScrollCanvas, orient=HORIZONTAL, command = httpMitmErrorOutputScrollCanvas.xview)
            httpMitmErrorOutputHorizontalScrollbar.pack(side = BOTTOM, fill = X)

            httpMitmErrorOutputScrollCanvas.configure(yscrollcommand=httpMitmErrorOutputVerticalScrollbar.set)
            httpMitmErrorOutputScrollCanvas.bind("<Configure>", lambda e : httpMitmErrorOutputScrollCanvas.configure(scrollregion=httpMitmErrorOutputScrollCanvas.bbox("all")))
            httpMitmErrorOutputFrame.bind_all("<MouseWheel>", lambda e : httpMitmErrorOutputScrollCanvas.yview_scroll(-1, "units"))

            httpMitmErrorOutputScrollCanvas.configure(xscrollcommand=httpMitmErrorOutputHorizontalScrollbar.set)
            httpMitmErrorOutputScrollCanvas.bind("<Configure>", lambda e : httpMitmErrorOutputScrollCanvas.configure(scrollregion=httpMitmErrorOutputScrollCanvas.bbox("all")))
            httpMitmErrorOutputFrame.bind_all("<MouseWheel>", lambda e : httpMitmErrorOutputScrollCanvas.xview_scroll(-1, "units"))

            self.httpMitmErrorOutputContentFrame = Frame(httpMitmErrorOutputScrollCanvas, background="#252525", highlightbackground="#ffffff")
            httpMitmErrorOutputScrollCanvas.create_window((0,0), window = self.httpMitmErrorOutputContentFrame, anchor = NW)
            self.httpMitmErrorOutputContentFrame.bind("<Configure>", lambda e : httpMitmErrorOutputScrollCanvas.configure(scrollregion=httpMitmErrorOutputScrollCanvas.bbox("all")))

        elif chosenAttackType == "WPA/WPA2-Cracking" :
            wpaWpa2CrackFrame = Frame(self.attacksScrollFrame, width=1280, height=200, background="#612601", borderwidth=3, relief="raised")
            wpaWpa2CrackFrame.pack()

            wpaWpa2CrackLabel = Label(wpaWpa2CrackFrame, text=" WPA / WPA2 Cracking ", fg="#ffffff", bg="#2E1201", font="bahnschrift 12")
            wpaWpa2CrackLabel.place(x=0, y=0)

            wpaWpa2CrackInterfaceLabel = Label(wpaWpa2CrackFrame, text="Interface                         :", fg="#ffffff", bg="#612601", font="bahnschrift 12")
            wpaWpa2CrackInterfaceLabel.place(x = 10, y = 48)

            self.wpaWpa2CrackInterfaceEntry = Entry(wpaWpa2CrackFrame, width = 20, font="bahnschrift 12", fg="#ffffff", bg="#252525")
            self.wpaWpa2CrackInterfaceEntry.place(x = 300, y = 48)

            wpaWpa2CrackTargetBssidLabel = Label(wpaWpa2CrackFrame, text="Target BSSID                  :", fg="#ffffff", bg="#612601", font="bahnschrift 12")
            wpaWpa2CrackTargetBssidLabel.place(x = 10, y = 98)

            self.wpaWpa2CrackTargetBssidEntry = Entry(wpaWpa2CrackFrame, width = 20, font="bahnschrift 12", fg="#ffffff", bg="#252525")
            self.wpaWpa2CrackTargetBssidEntry.place(x = 300, y = 98)

            wpaWpa2CrackTargetChannelLabel = Label(wpaWpa2CrackFrame, text="Target Channel               :", fg="#ffffff", bg="#612601", font="bahnschrift 12")
            wpaWpa2CrackTargetChannelLabel.place(x = 10, y = 148)

            self.wpaWpa2CrackTargetChannelEntry = Entry(wpaWpa2CrackFrame, width = 20, font="bahnschrift 12", fg="#ffffff", bg="#252525")
            self.wpaWpa2CrackTargetChannelEntry.place(x = 300, y = 148)



            wpaWpa2CrackTerminalLabel = Label(wpaWpa2CrackFrame, text="Terminal", fg="#ffffff", bg="#612601", font="bahnschrift 15")
            wpaWpa2CrackTerminalLabel.place(x = 660, y = 20)

            wpaWpa2CrackTerminalFrame = Frame(wpaWpa2CrackFrame, width=300, height=120, background="#252525", highlightbackground="#ffffff", highlightthickness=2)
            wpaWpa2CrackTerminalFrame.pack_propagate(False)
            wpaWpa2CrackTerminalFrame.place(x = 555, y = 55)

            wpaWpa2CrackTerminalScrollCanvas = Canvas(wpaWpa2CrackTerminalFrame, background="#252525", highlightbackground="#ffffff", yscrollincrement=8)
            wpaWpa2CrackTerminalScrollCanvas.pack(side = LEFT, fill = BOTH, expand = 1)
        
            wpaWpa2CrackTerminalVerticalScrollbar = Scrollbar(wpaWpa2CrackTerminalScrollCanvas, orient=VERTICAL, command = wpaWpa2CrackTerminalScrollCanvas.yview)
            wpaWpa2CrackTerminalVerticalScrollbar.pack(side = RIGHT, fill = Y)

            wpaWpa2CrackTerminalHorizontalScrollbar = Scrollbar(wpaWpa2CrackTerminalScrollCanvas, orient=HORIZONTAL, command = wpaWpa2CrackTerminalScrollCanvas.xview)
            wpaWpa2CrackTerminalHorizontalScrollbar.pack(side = BOTTOM, fill = X)

            wpaWpa2CrackTerminalScrollCanvas.configure(yscrollcommand=wpaWpa2CrackTerminalVerticalScrollbar.set)
            wpaWpa2CrackTerminalScrollCanvas.bind("<Configure>", lambda e : wpaWpa2CrackTerminalScrollCanvas.configure(scrollregion=wpaWpa2CrackTerminalScrollCanvas.bbox("all")))
            wpaWpa2CrackTerminalScrollCanvas.bind_all("<MouseWheel>", lambda e : wpaWpa2CrackTerminalScrollCanvas.yview_scroll(-1, "units"))

            wpaWpa2CrackTerminalScrollCanvas.configure(xscrollcommand=wpaWpa2CrackTerminalHorizontalScrollbar.set)
            wpaWpa2CrackTerminalScrollCanvas.bind("<Configure>", lambda e : wpaWpa2CrackTerminalScrollCanvas.configure(scrollregion=wpaWpa2CrackTerminalScrollCanvas.bbox("all")))
            wpaWpa2CrackTerminalScrollCanvas.bind_all("<MouseWheel>", lambda e : wpaWpa2CrackTerminalScrollCanvas.xview_scroll(-1, "units"))

            self.wpaWpa2CrackTerminalContentFrame = Frame(wpaWpa2CrackTerminalScrollCanvas, background="#252525", highlightbackground="#ffffff")
            wpaWpa2CrackTerminalScrollCanvas.create_window((0,0), window = self.wpaWpa2CrackTerminalContentFrame, anchor = NW)
            self.wpaWpa2CrackTerminalContentFrame.bind("<Configure>", lambda e : wpaWpa2CrackTerminalScrollCanvas.configure(scrollregion=wpaWpa2CrackTerminalScrollCanvas.bbox("all")))



            wpaWpa2CrackErrorLabel = Label(wpaWpa2CrackFrame, text="Errors", fg="#ffffff", bg="#612601", font="bahnschrift 15")
            wpaWpa2CrackErrorLabel.place(x = 1035, y = 20)

            wpaWpa2CrackErrorOutputFrame = Frame(wpaWpa2CrackFrame, width=300, height=120, background="#252525", highlightbackground="#ffffff", highlightthickness=2)
            wpaWpa2CrackErrorOutputFrame.pack_propagate(False)
            wpaWpa2CrackErrorOutputFrame.place(x = 915, y = 55)

            wpaWpa2CrackErrorOutputScrollCanvas = Canvas(wpaWpa2CrackErrorOutputFrame, background="#252525", highlightbackground="#ffffff", yscrollincrement=8)
            wpaWpa2CrackErrorOutputScrollCanvas.pack(side = LEFT, fill = BOTH, expand=1)
        
            wpaWpa2CrackErrorOutputVerticalScrollbar = Scrollbar(wpaWpa2CrackErrorOutputScrollCanvas, orient=VERTICAL, command = wpaWpa2CrackErrorOutputScrollCanvas.yview)
            wpaWpa2CrackErrorOutputVerticalScrollbar.pack(side = RIGHT, fill = Y)

            wpaWpa2CrackErrorOutputHorizontalScrollbar = Scrollbar(wpaWpa2CrackErrorOutputScrollCanvas, orient=HORIZONTAL, command = wpaWpa2CrackErrorOutputScrollCanvas.xview)
            wpaWpa2CrackErrorOutputHorizontalScrollbar.pack(side = BOTTOM, fill = X)

            wpaWpa2CrackErrorOutputScrollCanvas.configure(yscrollcommand=wpaWpa2CrackErrorOutputVerticalScrollbar.set)
            wpaWpa2CrackErrorOutputScrollCanvas.bind("<Configure>", lambda e : wpaWpa2CrackErrorOutputScrollCanvas.configure(scrollregion=wpaWpa2CrackErrorOutputScrollCanvas.bbox("all")))
            wpaWpa2CrackErrorOutputFrame.bind_all("<MouseWheel>", lambda e : wpaWpa2CrackErrorOutputScrollCanvas.yview_scroll(-1, "units"))

            wpaWpa2CrackErrorOutputScrollCanvas.configure(xscrollcommand=wpaWpa2CrackErrorOutputHorizontalScrollbar.set)
            wpaWpa2CrackErrorOutputScrollCanvas.bind("<Configure>", lambda e : wpaWpa2CrackErrorOutputScrollCanvas.configure(scrollregion=wpaWpa2CrackErrorOutputScrollCanvas.bbox("all")))
            wpaWpa2CrackErrorOutputFrame.bind_all("<MouseWheel>", lambda e : wpaWpa2CrackErrorOutputScrollCanvas.xview_scroll(-1, "units"))

            self.wpaWpa2CrackErrorOutputContentFrame = Frame(wpaWpa2CrackErrorOutputScrollCanvas, background="#252525", highlightbackground="#ffffff")
            wpaWpa2CrackErrorOutputScrollCanvas.create_window((0,0), window = self.wpaWpa2CrackErrorOutputContentFrame, anchor = NW)
            self.wpaWpa2CrackErrorOutputContentFrame.bind("<Configure>", lambda e : wpaWpa2CrackErrorOutputScrollCanvas.configure(scrollregion=wpaWpa2CrackErrorOutputScrollCanvas.bbox("all")))

        self.chosenAttackTypes.append(chosenAttackType)

    def executeChainAttack(self) :
        self.chainAttackThreads = []
        for attackTypes in self.chosenAttackTypes :
            if attackTypes == "CAM Table Overflow" :
                self.camThreads = threading.Thread(target = lambda : startCam(self.camTargetIpEntry.get(), self.camPacketNumberEntry.get(), self.camTerminalContentFrame, self.camErrorOutputContentFrame))
                self.chainAttackThreads.append(self.camThreads)
            elif attackTypes == "DHCP Starvation Attack" :
                self.dhcpThreads = threading.Thread(target = lambda : startDhcp(self.dhcpAttackInterfaceEntry.get(), self.dhcpAttackTerminalContentFrame, self.dhcpAttackErrorOutputContentFrame))
                self.chainAttackThreads.append(self.dhcpThreads)
            elif attackTypes == "ARP Poisoning Attack" :
                self.arpPoisonThreads = threading.Thread(target = lambda : startArp(self.arpPoisonTargetIpEntry.get(), self.arpPoisonDefaultGateEntry.get(), self.arpPoisonTerminalContentFrame, self.arpPoisonErrorOutputContentFrame))
                self.chainAttackThreads.append(self.arpPoisonThreads)
            elif attackTypes == "MAC Address Spoofing" :
                self.macAddressSpoofThreads = threading.Thread(target = lambda : startMac(self.macAddressSpoofTerminalContentFrame, self.macAddressSpoofErrorOutputContentFrame))
                self.chainAttackThreads.append(self.macAddressSpoofThreads)

            elif attackTypes == "Syn Flooding" :
                self.synFloodThreads = threading.Thread(target = lambda : startSynFlood(self.synFloodTargetIpEntry.get(), self.synFloodPortEntry.get(), self.synFloodTerminalContentFrame, self.synFloodErrorOutputContentFrame))
                self.chainAttackThreads.append(self.synFloodThreads)
            elif attackTypes == "ICMP Attack" :
                self.icmpThreads = threading.Thread(target = lambda : startIcmpAttack(self.icmpAttackTargetIpEntry.get(), self.icmpAttackTerminalContentFrame, self.icmpAttackErrorOutputContentFrame))
                self.chainAttackThreads.append(self.icmpThreads)

            elif attackTypes == "DNS Amplification" :
                self.dnsAmpThreads = threading.Thread(target = lambda : startDnsAmplification(self.dnsAmpTargetIpEntry.get(), self.dnsAmpPacketEntry.get(), self.dnsAmpTerminalContentFrame, self.dnsAmpErrorOutputContentFrame))
                self.chainAttackThreads.append(self.dnsAmpThreads)
            elif attackTypes == "DNS Spoofing" :
                self.dnsSpoofThreads = threading.Thread(target = lambda : startDnsSpoofing(self.dnsSpoofInterfaceEntry, self.dnsSpoofTargetIpEntry.get(), self.dnsSpoofTargetDomainsEntry, self.dnsSpoofTerminalContentFrame, self.dnsSpoofErrorOutputContentFrame))
                self.chainAttackThreads.append(self.dnsSpoofThreads)

            elif attackTypes == "HTTP-Man-In-The-Middle" :
                self.httpMitmThreads = threading.Thread(target = lambda : startHttpMitm(self.httpMitmInterfaceEntry.get(), self.httpMitmTerminalContentFrame, self.httpMitmErrorOutputContentFrame))
                self.chainAttackThreads.append(self.httpMitmThreads)

            elif attackTypes == "WPA/WPA2-Cracking" :
                self.wpaWpa2CrackThreads = threading.Thread(target = lambda : startWpaWpa2Cracking(self.wpaWpa2CrackInterfaceEntry.get(), self.wpaWpa2CrackTargetBssidEntry.get(), self.wpaWpa2CrackTargetChannelEntry.get(), self.wpaWpa2CrackTerminalContentFrame, self.wpaWpa2CrackErrorOutputContentFrame))
                self.chainAttackThreads.append(self.wpaWpa2CrackThreads)
        
        for thread in self.chainAttackThreads :
            thread.start()
    
    def terminateChainAttack(self) :
        for attackTypes in self.chosenAttackTypes :
            if attackTypes == "CAM Table Overflow" :
                self.camThreads.join(0)
                self.camThreads = None
            elif attackTypes == "DHCP Starvation Attack" :
                self.dhcpThreads.join(0)
                self.dhcpThreads = None
            elif attackTypes == "ARP Poisoning Attack" :
                self.arpPoisonThreads.join(0)
                self.arpPoisonThreads = None
            elif attackTypes == "MAC Address Spoofing" :
                self.macAddressSpoofThreads.join(0)
                self.macAddressSpoofThreads = None

            elif attackTypes == "Syn Flooding" :
                self.synFloodThreads.join(0)
                self.synFloodThreads = None
            elif attackTypes == "ICMP Attack" :
                self.icmpThreads.join(0)
                self.icmpThreads = None

            elif attackTypes == "DNS Amplification" :
                self.dnsAmpThreads.join(0)
                self.dnsAmpThreads = None
            elif attackTypes == "DNS Spoofing" :
                self.dnsSpoofThreads.join(0)
                self.dnsSpoofThreads = None

            elif attackTypes == "HTTP-Man-In-The-Middle" :
                self.httpMitmThreads.join(0)
                self.httpMitmThreads = None

            elif attackTypes == "WPA/WPA2-Cracking" :
                self.wpaWpa2CrackThreads.join(0)
                self.wpaWpa2CrackThreads = None
