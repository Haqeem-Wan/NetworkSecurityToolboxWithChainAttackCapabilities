from tkinter import *
from tkinter.ttk import Combobox, Style
import threading

from Layer2Attacks.PageCamAttacks.FrameCam import *
from Layer2Attacks.PageArpAttacks.FrameArp import *
from DnsAttacks.PageDnsAmplification.FrameDnsAmplification import *

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
            "DHCP Attack",
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
                "DHCP Attack",
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
            self.camFrame = Frame(self.attacksScrollFrame, width=1280, height=200, background="#612601", borderwidth=3, relief="raised")
            self.camFrame.pack()

            self.camLabel = Label(self.camFrame, text=" CAM Table Overflow ", fg="#ffffff", bg="#2E1201", font="bahnschrift 12")
            self.camLabel.place(x=0, y=0)

            self.camTargetIpLabel = Label(self.camFrame, text="Target IP Address                    :", fg="#ffffff", bg="#612601", font="bahnschrift 12")
            self.camTargetIpLabel.place(x = 10, y = 70)

            self.camTargetIpEntry = Entry(self.camFrame, width = 20, font="bahnschrift 12", fg="#ffffff", bg="#252525")
            self.camTargetIpEntry.place(x = 300, y = 70)

            self.camPacketNumberLabel = Label(self.camFrame, text="Number of Packets to send     :", fg="#ffffff", bg="#612601", font="bahnschrift 12")
            self.camPacketNumberLabel.place(x = 10, y = 120)

            self.camPacketNumberEntry = Entry(self.camFrame, width = 20, font="bahnschrift 12", fg="#ffffff", bg="#252525")
            self.camPacketNumberEntry.place(x = 300, y = 120)



            self.camTerminalLabel = Label(self.camFrame, text="Terminal", fg="#ffffff", bg="#612601", font="bahnschrift 15")
            self.camTerminalLabel.place(x = 660, y = 20)

            self.camTerminalFrame = Frame(self.camFrame, width=300, height=120, background="#252525", highlightbackground="#ffffff", highlightthickness=2)
            self.camTerminalFrame.pack_propagate(False)
            self.camTerminalFrame.place(x = 555, y = 55)

            self.camTerminalScrollCanvas = Canvas(self.camTerminalFrame, background="#252525", highlightbackground="#ffffff", yscrollincrement=8)
            self.camTerminalScrollCanvas.pack(side = LEFT, fill = BOTH, expand = 1)
        
            self.camTerminalVerticalScrollbar = Scrollbar(self.camTerminalScrollCanvas, orient=VERTICAL, command = self.camTerminalScrollCanvas.yview)
            self.camTerminalVerticalScrollbar.pack(side = RIGHT, fill = Y)

            self.camTerminalHorizontalScrollbar = Scrollbar(self.camTerminalScrollCanvas, orient=HORIZONTAL, command = self.camTerminalScrollCanvas.xview)
            self.camTerminalHorizontalScrollbar.pack(side = BOTTOM, fill = X)

            self.camTerminalScrollCanvas.configure(yscrollcommand=self.camTerminalVerticalScrollbar.set)
            self.camTerminalScrollCanvas.bind("<Configure>", lambda e : self.camTerminalScrollCanvas.configure(scrollregion=self.camTerminalScrollCanvas.bbox("all")))
            self.camTerminalScrollCanvas.bind_all("<MouseWheel>", lambda e : self.camTerminalScrollCanvas.yview_scroll(-1, "units"))

            self.camTerminalScrollCanvas.configure(xscrollcommand=self.camTerminalHorizontalScrollbar.set)
            self.camTerminalScrollCanvas.bind("<Configure>", lambda e : self.camTerminalScrollCanvas.configure(scrollregion=self.camTerminalScrollCanvas.bbox("all")))
            self.camTerminalScrollCanvas.bind_all("<MouseWheel>", lambda e : self.camTerminalScrollCanvas.xview_scroll(-1, "units"))

            self.camTerminalContentFrame = Frame(self.camTerminalScrollCanvas, background="#252525", highlightbackground="#ffffff")
            self.camTerminalScrollCanvas.create_window((0,0), window = self.camTerminalContentFrame, anchor = NW)
            self.camTerminalContentFrame.bind("<Configure>", lambda e : self.camTerminalScrollCanvas.configure(scrollregion=self.camTerminalScrollCanvas.bbox("all")))



            self.camErrorLabel = Label(self.camFrame, text="Errors", fg="#ffffff", bg="#612601", font="bahnschrift 15")
            self.camErrorLabel.place(x = 1035, y = 20)

            self.camErrorOutputFrame = Frame(self.camFrame, width=300, height=120, background="#252525", highlightbackground="#ffffff", highlightthickness=2)
            self.camErrorOutputFrame.pack_propagate(False)
            self.camErrorOutputFrame.place(x = 915, y = 55)

            self.camErrorOutputScrollCanvas = Canvas(self.camErrorOutputFrame, background="#252525", highlightbackground="#ffffff", yscrollincrement=8)
            self.camErrorOutputScrollCanvas.pack(side = LEFT, fill = BOTH, expand=1)
        
            self.camErrorOutputVerticalScrollbar = Scrollbar(self.camErrorOutputScrollCanvas, orient=VERTICAL, command = self.camErrorOutputScrollCanvas.yview)
            self.camErrorOutputVerticalScrollbar.pack(side = RIGHT, fill = Y)

            self.camErrorOutputHorizontalScrollbar = Scrollbar(self.camErrorOutputScrollCanvas, orient=HORIZONTAL, command = self.camErrorOutputScrollCanvas.xview)
            self.camErrorOutputHorizontalScrollbar.pack(side = BOTTOM, fill = X)

            self.camErrorOutputScrollCanvas.configure(yscrollcommand=self.camErrorOutputVerticalScrollbar.set)
            self.camErrorOutputScrollCanvas.bind("<Configure>", lambda e : self.camErrorOutputScrollCanvas.configure(scrollregion=self.camErrorOutputScrollCanvas.bbox("all")))
            self.camErrorOutputFrame.bind_all("<MouseWheel>", lambda e : self.camErrorOutputScrollCanvas.yview_scroll(-1, "units"))

            self.camErrorOutputScrollCanvas.configure(xscrollcommand=self.camErrorOutputHorizontalScrollbar.set)
            self.camErrorOutputScrollCanvas.bind("<Configure>", lambda e : self.camErrorOutputScrollCanvas.configure(scrollregion=self.camErrorOutputScrollCanvas.bbox("all")))
            self.camErrorOutputFrame.bind_all("<MouseWheel>", lambda e : self.camErrorOutputScrollCanvas.xview_scroll(-1, "units"))

            self.camErrorOutputContentFrame = Frame(self.camErrorOutputScrollCanvas, background="#252525", highlightbackground="#ffffff")
            self.camErrorOutputScrollCanvas.create_window((0,0), window = self.camErrorOutputContentFrame, anchor = NW)
            self.camErrorOutputContentFrame.bind("<Configure>", lambda e : self.camErrorOutputScrollCanvas.configure(scrollregion=self.camErrorOutputScrollCanvas.bbox("all")))
            '''
            # Cannot get it to delete multiple iterations of the same attack
            self.removeCamButton = Button(self.camFrame, height=1, width=1, font="bahnschrift 15", 
                                          text="X", fg="#ffffff", bg="#612601", command=lambda : self.deleteFrame(self.camFrame))
            self.removeCamButton.place(x=1222,y=155)
            '''
            #self.camFrame.pack()
        
        elif chosenAttackType == "ARP Poisoning Attack" :
            self.arpPoisonFrame = Frame(self.attacksScrollFrame, width=1280, height=200, background="#612601", borderwidth=3, relief="raised")
            self.arpPoisonFrame.pack()

            self.arpPoisonLabel = Label(self.arpPoisonFrame, text=" ARP Poisoning Attack ", fg="#ffffff", bg="#2E1201", font="bahnschrift 12")
            self.arpPoisonLabel.place(x=0, y=0)

            self.arpPoisonTargetIpLabel = Label(self.arpPoisonFrame, text="Target IP Address                    :", fg="#ffffff", bg="#612601", font="bahnschrift 12")
            self.arpPoisonTargetIpLabel.place(x = 10, y = 70)

            self.arpPoisonTargetIpEntry = Entry(self.arpPoisonFrame, width = 20, font="bahnschrift 12", fg="#ffffff", bg="#252525")
            self.arpPoisonTargetIpEntry.place(x = 300, y = 70)

            self.arpPoisonDefaultGateLabel = Label(self.arpPoisonFrame, text="Target Default Gateway   :", fg="#ffffff", bg="#612601", font="bahnschrift 12")
            self.arpPoisonDefaultGateLabel.place(x = 10, y = 120)

            self.arpPoisonDefaultGateEntry = Entry(self.arpPoisonFrame, width = 20, font="bahnschrift 12", fg="#ffffff", bg="#252525")
            self.arpPoisonDefaultGateEntry.place(x = 300, y = 120)



            self.arpPoisonTerminalLabel = Label(self.arpPoisonFrame, text="Terminal", fg="#ffffff", bg="#612601", font="bahnschrift 15")
            self.arpPoisonTerminalLabel.place(x = 660, y = 20)

            self.arpPoisonTerminalFrame = Frame(self.arpPoisonFrame, width=300, height=120, background="#252525", highlightbackground="#ffffff", highlightthickness=2)
            self.arpPoisonTerminalFrame.pack_propagate(False)
            self.arpPoisonTerminalFrame.place(x = 555, y = 55)

            self.arpPoisonTerminalScrollCanvas = Canvas(self.arpPoisonTerminalFrame, background="#252525", highlightbackground="#ffffff", yscrollincrement=8)
            self.arpPoisonTerminalScrollCanvas.pack(side = LEFT, fill = BOTH, expand = 1)
        
            self.arpPoisonTerminalVerticalScrollbar = Scrollbar(self.arpPoisonTerminalScrollCanvas, orient=VERTICAL, command = self.arpPoisonTerminalScrollCanvas.yview)
            self.arpPoisonTerminalVerticalScrollbar.pack(side = RIGHT, fill = Y)

            self.arpPoisonTerminalHorizontalScrollbar = Scrollbar(self.arpPoisonTerminalScrollCanvas, orient=HORIZONTAL, command = self.arpPoisonTerminalScrollCanvas.xview)
            self.arpPoisonTerminalHorizontalScrollbar.pack(side = BOTTOM, fill = X)

            self.arpPoisonTerminalScrollCanvas.configure(yscrollcommand=self.arpPoisonTerminalVerticalScrollbar.set)
            self.arpPoisonTerminalScrollCanvas.bind("<Configure>", lambda e : self.arpPoisonTerminalScrollCanvas.configure(scrollregion=self.arpPoisonTerminalScrollCanvas.bbox("all")))
            self.arpPoisonTerminalScrollCanvas.bind_all("<MouseWheel>", lambda e : self.arpPoisonTerminalScrollCanvas.yview_scroll(-1, "units"))

            self.arpPoisonTerminalScrollCanvas.configure(xscrollcommand=self.arpPoisonTerminalHorizontalScrollbar.set)
            self.arpPoisonTerminalScrollCanvas.bind("<Configure>", lambda e : self.arpPoisonTerminalScrollCanvas.configure(scrollregion=self.arpPoisonTerminalScrollCanvas.bbox("all")))
            self.arpPoisonTerminalScrollCanvas.bind_all("<MouseWheel>", lambda e : self.arpPoisonTerminalScrollCanvas.xview_scroll(-1, "units"))

            self.arpPoisonTerminalContentFrame = Frame(self.arpPoisonTerminalScrollCanvas, background="#252525", highlightbackground="#ffffff")
            self.arpPoisonTerminalScrollCanvas.create_window((0,0), window = self.arpPoisonTerminalContentFrame, anchor = NW)
            self.arpPoisonTerminalContentFrame.bind("<Configure>", lambda e : self.arpPoisonTerminalScrollCanvas.configure(scrollregion=self.arpPoisonTerminalScrollCanvas.bbox("all")))



            self.arpPoisonErrorLabel = Label(self.arpPoisonFrame, text="Errors", fg="#ffffff", bg="#612601", font="bahnschrift 15")
            self.arpPoisonErrorLabel.place(x = 1035, y = 20)

            self.arpPoisonErrorOutputFrame = Frame(self.arpPoisonFrame, width=300, height=120, background="#252525", highlightbackground="#ffffff", highlightthickness=2)
            self.arpPoisonErrorOutputFrame.pack_propagate(False)
            self.arpPoisonErrorOutputFrame.place(x = 915, y = 55)

            self.arpPoisonErrorOutputScrollCanvas = Canvas(self.arpPoisonErrorOutputFrame, background="#252525", highlightbackground="#ffffff", yscrollincrement=8)
            self.arpPoisonErrorOutputScrollCanvas.pack(side = LEFT, fill = BOTH, expand=1)
        
            self.arpPoisonErrorOutputVerticalScrollbar = Scrollbar(self.arpPoisonErrorOutputScrollCanvas, orient=VERTICAL, command = self.arpPoisonErrorOutputScrollCanvas.yview)
            self.arpPoisonErrorOutputVerticalScrollbar.pack(side = RIGHT, fill = Y)

            self.arpPoisonErrorOutputHorizontalScrollbar = Scrollbar(self.arpPoisonErrorOutputScrollCanvas, orient=HORIZONTAL, command = self.arpPoisonErrorOutputScrollCanvas.xview)
            self.arpPoisonErrorOutputHorizontalScrollbar.pack(side = BOTTOM, fill = X)

            self.arpPoisonErrorOutputScrollCanvas.configure(yscrollcommand=self.arpPoisonErrorOutputVerticalScrollbar.set)
            self.arpPoisonErrorOutputScrollCanvas.bind("<Configure>", lambda e : self.arpPoisonErrorOutputScrollCanvas.configure(scrollregion=self.arpPoisonErrorOutputScrollCanvas.bbox("all")))
            self.arpPoisonErrorOutputFrame.bind_all("<MouseWheel>", lambda e : self.arpPoisonErrorOutputScrollCanvas.yview_scroll(-1, "units"))

            self.arpPoisonErrorOutputScrollCanvas.configure(xscrollcommand=self.arpPoisonErrorOutputHorizontalScrollbar.set)
            self.arpPoisonErrorOutputScrollCanvas.bind("<Configure>", lambda e : self.arpPoisonErrorOutputScrollCanvas.configure(scrollregion=self.arpPoisonErrorOutputScrollCanvas.bbox("all")))
            self.arpPoisonErrorOutputFrame.bind_all("<MouseWheel>", lambda e : self.arpPoisonErrorOutputScrollCanvas.xview_scroll(-1, "units"))

            self.arpPoisonErrorOutputContentFrame = Frame(self.arpPoisonErrorOutputScrollCanvas, background="#252525", highlightbackground="#ffffff")
            self.arpPoisonErrorOutputScrollCanvas.create_window((0,0), window = self.arpPoisonErrorOutputContentFrame, anchor = NW)
            self.arpPoisonErrorOutputContentFrame.bind("<Configure>", lambda e : self.arpPoisonErrorOutputScrollCanvas.configure(scrollregion=self.arpPoisonErrorOutputScrollCanvas.bbox("all")))
        
        elif chosenAttackType == "DNS Amplification" :
            self.dnsAmpFrame = Frame(self.attacksScrollFrame, width=1280, height=200, background="#612601", borderwidth=3, relief="raised")
            self.dnsAmpFrame.pack()

            self.dnsAmpLabel = Label(self.dnsAmpFrame, text=" DNS Amplification ", fg="#ffffff", bg="#2E1201", font="bahnschrift 12")
            self.dnsAmpLabel.place(x=0, y=0)

            self.dnsAmpTargetIpLabel = Label(self.dnsAmpFrame, text="Target IP Address                    :", fg="#ffffff", bg="#612601", font="bahnschrift 12")
            self.dnsAmpTargetIpLabel.place(x = 10, y = 70)

            self.dnsAmpTargetIpEntry = Entry(self.dnsAmpFrame, width = 20, font="bahnschrift 12", fg="#ffffff", bg="#252525")
            self.dnsAmpTargetIpEntry.place(x = 300, y = 70)

            self.dnsAmpPacketLabel = Label(self.dnsAmpFrame, text="DNS Packet Amount (Int)    :", fg="#ffffff", bg="#612601", font="bahnschrift 12")
            self.dnsAmpPacketLabel.place(x = 10, y = 120)

            self.dnsAmpPacketEntry = Entry(self.dnsAmpFrame, width = 20, font="bahnschrift 12", fg="#ffffff", bg="#252525")
            self.dnsAmpPacketEntry.place(x = 300, y = 120)



            self.dnsAmpTerminalLabel = Label(self.dnsAmpFrame, text="Terminal", fg="#ffffff", bg="#612601", font="bahnschrift 15")
            self.dnsAmpTerminalLabel.place(x = 660, y = 20)

            self.dnsAmpTerminalFrame = Frame(self.dnsAmpFrame, width=300, height=120, background="#252525", highlightbackground="#ffffff", highlightthickness=2)
            self.dnsAmpTerminalFrame.pack_propagate(False)
            self.dnsAmpTerminalFrame.place(x = 555, y = 55)

            self.dnsAmpTerminalScrollCanvas = Canvas(self.dnsAmpTerminalFrame, background="#252525", highlightbackground="#ffffff", yscrollincrement=8)
            self.dnsAmpTerminalScrollCanvas.pack(side = LEFT, fill = BOTH, expand = 1)
        
            self.dnsAmpTerminalVerticalScrollbar = Scrollbar(self.dnsAmpTerminalScrollCanvas, orient=VERTICAL, command = self.dnsAmpTerminalScrollCanvas.yview)
            self.dnsAmpTerminalVerticalScrollbar.pack(side = RIGHT, fill = Y)

            self.dnsAmpTerminalHorizontalScrollbar = Scrollbar(self.dnsAmpTerminalScrollCanvas, orient=HORIZONTAL, command = self.dnsAmpTerminalScrollCanvas.xview)
            self.dnsAmpTerminalHorizontalScrollbar.pack(side = BOTTOM, fill = X)

            self.dnsAmpTerminalScrollCanvas.configure(yscrollcommand=self.dnsAmpTerminalVerticalScrollbar.set)
            self.dnsAmpTerminalScrollCanvas.bind("<Configure>", lambda e : self.dnsAmpTerminalScrollCanvas.configure(scrollregion=self.dnsAmpTerminalScrollCanvas.bbox("all")))
            self.dnsAmpTerminalScrollCanvas.bind_all("<MouseWheel>", lambda e : self.dnsAmpTerminalScrollCanvas.yview_scroll(-1, "units"))

            self.dnsAmpTerminalScrollCanvas.configure(xscrollcommand=self.dnsAmpTerminalHorizontalScrollbar.set)
            self.dnsAmpTerminalScrollCanvas.bind("<Configure>", lambda e : self.dnsAmpTerminalScrollCanvas.configure(scrollregion=self.dnsAmpTerminalScrollCanvas.bbox("all")))
            self.dnsAmpTerminalScrollCanvas.bind_all("<MouseWheel>", lambda e : self.dnsAmpTerminalScrollCanvas.xview_scroll(-1, "units"))

            self.dnsAmpTerminalContentFrame = Frame(self.dnsAmpTerminalScrollCanvas, background="#252525", highlightbackground="#ffffff")
            self.dnsAmpTerminalScrollCanvas.create_window((0,0), window = self.dnsAmpTerminalContentFrame, anchor = NW)
            self.dnsAmpTerminalContentFrame.bind("<Configure>", lambda e : self.dnsAmpTerminalScrollCanvas.configure(scrollregion=self.dnsAmpTerminalScrollCanvas.bbox("all")))



            self.dnsAmpErrorLabel = Label(self.dnsAmpFrame, text="Errors", fg="#ffffff", bg="#612601", font="bahnschrift 15")
            self.dnsAmpErrorLabel.place(x = 1035, y = 20)

            self.dnsAmpErrorOutputFrame = Frame(self.dnsAmpFrame, width=300, height=120, background="#252525", highlightbackground="#ffffff", highlightthickness=2)
            self.dnsAmpErrorOutputFrame.pack_propagate(False)
            self.dnsAmpErrorOutputFrame.place(x = 915, y = 55)

            self.dnsAmpErrorOutputScrollCanvas = Canvas(self.dnsAmpErrorOutputFrame, background="#252525", highlightbackground="#ffffff", yscrollincrement=8)
            self.dnsAmpErrorOutputScrollCanvas.pack(side = LEFT, fill = BOTH, expand=1)
        
            self.dnsAmpErrorOutputVerticalScrollbar = Scrollbar(self.dnsAmpErrorOutputScrollCanvas, orient=VERTICAL, command = self.dnsAmpErrorOutputScrollCanvas.yview)
            self.dnsAmpErrorOutputVerticalScrollbar.pack(side = RIGHT, fill = Y)

            self.dnsAmpErrorOutputHorizontalScrollbar = Scrollbar(self.dnsAmpErrorOutputScrollCanvas, orient=HORIZONTAL, command = self.dnsAmpErrorOutputScrollCanvas.xview)
            self.dnsAmpErrorOutputHorizontalScrollbar.pack(side = BOTTOM, fill = X)

            self.dnsAmpErrorOutputScrollCanvas.configure(yscrollcommand=self.dnsAmpErrorOutputVerticalScrollbar.set)
            self.dnsAmpErrorOutputScrollCanvas.bind("<Configure>", lambda e : self.dnsAmpErrorOutputScrollCanvas.configure(scrollregion=self.dnsAmpErrorOutputScrollCanvas.bbox("all")))
            self.dnsAmpErrorOutputFrame.bind_all("<MouseWheel>", lambda e : self.dnsAmpErrorOutputScrollCanvas.yview_scroll(-1, "units"))

            self.dnsAmpErrorOutputScrollCanvas.configure(xscrollcommand=self.dnsAmpErrorOutputHorizontalScrollbar.set)
            self.dnsAmpErrorOutputScrollCanvas.bind("<Configure>", lambda e : self.dnsAmpErrorOutputScrollCanvas.configure(scrollregion=self.dnsAmpErrorOutputScrollCanvas.bbox("all")))
            self.dnsAmpErrorOutputFrame.bind_all("<MouseWheel>", lambda e : self.dnsAmpErrorOutputScrollCanvas.xview_scroll(-1, "units"))

            self.dnsAmpErrorOutputContentFrame = Frame(self.dnsAmpErrorOutputScrollCanvas, background="#252525", highlightbackground="#ffffff")
            self.dnsAmpErrorOutputScrollCanvas.create_window((0,0), window = self.dnsAmpErrorOutputContentFrame, anchor = NW)
            self.dnsAmpErrorOutputContentFrame.bind("<Configure>", lambda e : self.dnsAmpErrorOutputScrollCanvas.configure(scrollregion=self.dnsAmpErrorOutputScrollCanvas.bbox("all")))
        self.chosenAttackTypes.append(chosenAttackType)

    def executeChainAttack(self) :
        self.chainAttackThreads = []
        for attackTypes in self.chosenAttackTypes :
            if attackTypes == "CAM Table Overflow" :
                self.chainAttackThreads.append(threading.Thread(target = lambda : startCam(self.camTargetIpEntry.get(), self.camPacketNumberEntry.get(), self.camTerminalContentFrame, self.camErrorOutputContentFrame)))
            elif attackTypes == "VLAN Hopping" :
                pass
            elif attackTypes == "DHCP Attack" :
                pass
            elif attackTypes == "ARP Poisoning Attack" :
                self.chainAttackThreads.append(threading.Thread(target = lambda : startArp(self.arpPoisonTargetIpEntry.get(), self.arpPoisonDefaultGateEntry.get(), self.arpPoisonTerminalContentFrame, self.arpPoisonErrorOutputContentFrame)))
            elif attackTypes == "MAC Address Spoofing" :
                pass
            elif attackTypes == "STP Attack" :
                pass
            elif attackTypes == "ICMP Attack" :
                pass
            elif attackTypes == "SeqNum. Predic. Attack" :
                pass
            elif attackTypes == "TCP Session Hijacking" :
                pass
            elif attackTypes == "IP Spoofing" :
                pass
            elif attackTypes == "SSL Strip" :
                pass

            elif attackTypes == "DNS Amplification" :
                self.chainAttackThreads.append(threading.Thread(target = lambda : startDnsAmplification(self.dnsAmpTargetIpEntry.get(), self.dnsAmpPacketEntry.get(), self.dnsAmpTerminalContentFrame, self.dnsAmpErrorOutputContentFrame)))
            elif attackTypes == "DNS Tunneling" :
                pass
            elif attackTypes == "DNS Spoofing" :
                pass
            elif attackTypes == "DNS Hijacking" :
                pass

            elif attackTypes == "SQL Injection" :
                pass
            elif attackTypes == "Broken Authentication" :
                pass
            elif attackTypes == "Sensitive Data Exposure" :
                pass
            elif attackTypes == "Cross-Site Scripting (XSS)" :
                pass

            elif attackTypes == "Denial of Service (DoS)" :
                pass
            elif attackTypes == "Evil Twin Attack" :
                pass
            elif attackTypes == "WPA / WPA2 Cracking" :
                pass
        
        for thread in self.chainAttackThreads :
            thread.start()

    # FINISH THIS
    def terminateChainAttack(self) :
        for attackTypes in self.chosenAttackTypes :
            if attackTypes == "CAM Table Overflow" :
                pass
                #self.camThreads
            elif attackTypes == "ARP Poisoning Attack" :
                arpPoisonThreads = threading.Thread(target = lambda : startArp(self.arpPoisonTargetIpEntry.get(), self.arpPoisonDefaultGateEntry.get(), self.arpPoisonTerminalContentFrame, self.arpPoisonErrorOutputContentFrame))
                arpPoisonThreads.start()    