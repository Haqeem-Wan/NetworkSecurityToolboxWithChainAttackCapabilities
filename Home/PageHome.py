from tkinter import *
from tkinter.ttk import Separator
from PIL import ImageTk, Image
from GeneralTools.funcGeneralTools import *
from ProgramSetup.Footer import *

class PageHome:
    def __init__ (self, frame):
        self.homeFrame = frame
        self.homeCanvas = Canvas(self.homeFrame, width=1260, height=670, background="#2C2B2B", yscrollincrement=8)
        self.homeCanvas.pack(side = LEFT, fill=BOTH, expand=1)

        # Create Scrollbar for Home Frame
        self.homeScrollbar = Scrollbar(self.homeFrame, orient=VERTICAL, command=self.homeCanvas.yview)
        self.homeScrollbar.pack(side = RIGHT, fill = Y)

        self.homeCanvas.configure(yscrollcommand=self.homeScrollbar.set)
        self.homeCanvas.bind("<Configure>", lambda e : self.homeCanvas.configure(scrollregion=self.homeCanvas.bbox("all")))
        self.homeCanvas.bind_all("<MouseWheel>", lambda e : self.homeCanvas.yview_scroll(-1, "units"))

        self.homeScrollFrame = Frame(self.homeCanvas, background="#252525", highlightbackground="#ffffff")
        self.homeCanvas.create_window((0,0), window = self.homeScrollFrame, anchor = NW)
        self.homeScrollFrame.bind("<Configure>", lambda e : self.homeCanvas.configure(scrollregion=self.homeCanvas.bbox("all")))

        # Title Frame
        self.homeTitleFrame = Frame(self.homeScrollFrame, width=1280, height=90, 
                                background="#2C2B2B", borderwidth=3, relief="raised")
        
        self.homeTitleLabel = Label(self.homeTitleFrame, text="HackerBox", fg="#ffffff", bg="#2C2B2B", font="bahnschrift 30 bold")
        self.homeTitleLabel.place(x=525, y=16)
        
        # Project Details Frame
        self.projDetFrame = Frame(self.homeScrollFrame, width=1280, height=385,
                                         background="#383838", borderwidth=2, relief="groove")
        
        self.projDetTitleLabel = Label(self.projDetFrame, text="FINAL YEAR PROJECT DETAILS", fg="#CFCFCF", 
                                        bg="#383838", font="bahnschrift 15 bold")
        self.projDetTitleLabel.place(x=10, y=10)

        self.projDetSeparator = Separator(self.projDetFrame, orient="horizontal")
        self.projDetSeparator.place(y=45, relwidth=1)

        self.projDetTopicTitleLabel = Label(self.projDetFrame, text="Topic", fg="#CFCFCF", 
                                            bg="#383838", font="bahnschrift 12")
        self.projDetTopicTitleLabel.place(x=50, y=65)

        self.projDetTopicColonLabel = Label(self.projDetFrame, text=":", fg="#CFCFCF", 
                                            bg="#383838", font="bahnschrift 12")
        self.projDetTopicColonLabel.place(x=235, y=65)

        self.projDetTopicTextLabel = Label(self.projDetFrame, text="NETWORK SECURITY TOOLBOX WITH CHAIN ATTACK CAPABILITIES", fg="#CFCFCF", 
                                            bg="#383838", font="bahnschrift 12")
        self.projDetTopicTextLabel.place(x=300, y=65)

        self.projDetSupervisorTitleLabel = Label(self.projDetFrame, text="Supervisor", fg="#CFCFCF", 
                                            bg="#383838", font="bahnschrift 12")
        self.projDetSupervisorTitleLabel.place(x=50, y=105)

        self.projDetSupervisorColonLabel = Label(self.projDetFrame, text=":", fg="#CFCFCF", 
                                            bg="#383838", font="bahnschrift 12")
        self.projDetSupervisorColonLabel.place(x=235, y=105)

        self.projDetSupervisorTextLabel = Label(self.projDetFrame, text="TS. DR. TIMOTHY YAP TZEN VUN", fg="#CFCFCF", 
                                            bg="#383838", font="bahnschrift 12")
        self.projDetSupervisorTextLabel.place(x=300, y=105)

        self.projDetStudentNameTitleLabel = Label(self.projDetFrame, text="Student Name", fg="#CFCFCF", 
                                            bg="#383838", font="bahnschrift 12")
        self.projDetStudentNameTitleLabel.place(x=50, y=145)

        self.projDetStudentNameColonLabel = Label(self.projDetFrame, text=":", fg="#CFCFCF", 
                                            bg="#383838", font="bahnschrift 12")
        self.projDetStudentNameColonLabel.place(x=235, y=145)

        self.projDetStudentNameTextLabel = Label(self.projDetFrame, text="WAN NASHRUL HAQEEM BIN WAN KAMAL", fg="#CFCFCF", 
                                            bg="#383838", font="bahnschrift 12")
        self.projDetStudentNameTextLabel.place(x=300, y=145)

        self.projDetStudentIdTitleLabel = Label(self.projDetFrame, text="Student ID", fg="#CFCFCF", 
                                            bg="#383838", font="bahnschrift 12")
        self.projDetStudentIdTitleLabel.place(x=50, y=185)

        self.projDetStudentIdColonLabel = Label(self.projDetFrame, text=":", fg="#CFCFCF", 
                                            bg="#383838", font="bahnschrift 12")
        self.projDetStudentIdColonLabel.place(x=235, y=185)

        self.projDetStudentIdTextLabel = Label(self.projDetFrame, text="1191102618", fg="#CFCFCF", 
                                            bg="#383838", font="bahnschrift 12")
        self.projDetStudentIdTextLabel.place(x=300, y=185)

        self.projDetStudentDegreeTitleLabel = Label(self.projDetFrame, text="Degree", fg="#CFCFCF", 
                                            bg="#383838", font="bahnschrift 12")
        self.projDetStudentDegreeTitleLabel.place(x=50, y=225)

        self.projDetStudentDegreeColonLabel = Label(self.projDetFrame, text=":", fg="#CFCFCF", 
                                            bg="#383838", font="bahnschrift 12")
        self.projDetStudentDegreeColonLabel.place(x=235, y=225)

        self.projDetStudentDegreeTextLabel = Label(self.projDetFrame, text="BACHELOR OF COMPUTER SCIENCE (HONS.)", fg="#CFCFCF", 
                                            bg="#383838", font="bahnschrift 12")
        self.projDetStudentDegreeTextLabel.place(x=300, y=225)

        self.projDetStudentSpecialTitleLabel = Label(self.projDetFrame, text="Specialization", fg="#CFCFCF", 
                                            bg="#383838", font="bahnschrift 12")
        self.projDetStudentSpecialTitleLabel.place(x=50, y=265)

        self.projDetStudentSpecialColonLabel = Label(self.projDetFrame, text=":", fg="#CFCFCF", 
                                            bg="#383838", font="bahnschrift 12")
        self.projDetStudentSpecialColonLabel.place(x=235, y=265)

        self.projDetStudentSpecialTextLabel = Label(self.projDetFrame, text="CYBERSECURITY", fg="#CFCFCF", 
                                            bg="#383838", font="bahnschrift 12")
        self.projDetStudentSpecialTextLabel.place(x=300, y=265)

        self.projDetContactNumberTitleLabel = Label(self.projDetFrame, text="Contact Number", fg="#CFCFCF", 
                                            bg="#383838", font="bahnschrift 12")
        self.projDetContactNumberTitleLabel.place(x=50, y=305)

        self.projDetContactNumberColonLabel = Label(self.projDetFrame, text=":", fg="#CFCFCF", 
                                            bg="#383838", font="bahnschrift 12")
        self.projDetContactNumberColonLabel.place(x=235, y=305)

        self.projDetContactNumberTextLabel = Label(self.projDetFrame, text="+60 17-290 3907", fg="#CFCFCF", 
                                            bg="#383838", font="bahnschrift 12")
        self.projDetContactNumberTextLabel.place(x=300, y=305)

        self.projDetStudentEmailTitleLabel = Label(self.projDetFrame, text="Student E-Mail", fg="#CFCFCF", 
                                            bg="#383838", font="bahnschrift 12")
        self.projDetStudentEmailTitleLabel.place(x=50, y=345)

        self.projDetStudentEmailColonLabel = Label(self.projDetFrame, text=":", fg="#CFCFCF", 
                                            bg="#383838", font="bahnschrift 12")
        self.projDetStudentEmailColonLabel.place(x=235, y=345)

        self.projDetStudentEmailTextLabel = Label(self.projDetFrame, text="1191102618@STUDENT.MMU.EDU.MY", fg="#CFCFCF", 
                                            bg="#383838", font="bahnschrift 12")
        self.projDetStudentEmailTextLabel.place(x=300, y=345)

        # How-To-Use Frame
        self.howToUseFrame = Frame(self.homeScrollFrame, width=1280, height=785,
                                         background="#444444", borderwidth=2, relief="groove")
        
        self.howToUseTitleLabel = Label(self.howToUseFrame, text="HOW TO USE THIS PROGRAM", fg="#CFCFCF", 
                                        bg="#444444", font="bahnschrift 15 bold")
        self.howToUseTitleLabel.place(x=10, y=10)

        self.howToUseSeparator = Separator(self.howToUseFrame, orient="horizontal")
        self.howToUseSeparator.place(y=45, relwidth=1)

        self.howToUseOneImage = PhotoImage(file = "img/howToUse_1.png")
        self.howToUseOneImageLabel = Label(self.howToUseFrame, image=self.howToUseOneImage) 
        self.howToUseOneImageLabel.place(x=50, y=60)

        self.howToUseOneImageLabel = Label(self.howToUseFrame, text="Click this box to access the Navigation Menu!", fg="#CFCFCF", 
                                            bg="#444444", font="bahnschrift 18")
        self.howToUseOneImageLabel.place(x=650, y=220)

        self.howToUseTwoImage = PhotoImage(file = "img/howToUse_2.png")
        self.howToUseTwoImageLabel = Label(self.howToUseFrame, image=self.howToUseTwoImage) 
        self.howToUseTwoImageLabel.place(x=655, y=425)

        self.howToUseOneImageLabel = Label(self.howToUseFrame, text="Click these to access the various Attack Pages!", fg="#CFCFCF", 
                                            bg="#444444", font="bahnschrift 18")
        self.howToUseOneImageLabel.place(x=40, y=575)

        # General Tools Frame
        self.generalToolsFrame = Frame(self.homeScrollFrame, width=1280, height=725,
                                        background="#535353", borderwidth=2, relief="groove")
        
        self.generalToolsTitleLabel = Label(self.generalToolsFrame, text="GENERAL TOOLS", fg="#CFCFCF", 
                                        bg="#535353", font="bahnschrift 15 bold")
        self.generalToolsTitleLabel.place(x=10, y=10)

        self.generalToolsSeparator = Separator(self.generalToolsFrame, orient="horizontal")
        self.generalToolsSeparator.place(y=45, relwidth=1)

        # Get IP Address
        self.generalToolsIpAddrTitleLabel = Label(self.generalToolsFrame, text="Get your IP Address!", fg="#CFCFCF", 
                                            bg="#535353", font="bahnschrift 15 bold")
        self.generalToolsIpAddrTitleLabel.place(x=50, y=65)

        self.generalToolsIpAddrEntry = Entry(self.generalToolsFrame, width = 10, font="bahnschrift 15", fg="#ffffff", bg="#252525")
        self.generalToolsIpAddrEntry.insert(0, "Interface")
        self.generalToolsIpAddrEntry.bind("<FocusIn>", self.on_click_ipaddr)
        self.generalToolsIpAddrEntry.bind("<FocusOut>", self.on_leave_ipaddr)
        self.generalToolsIpAddrEntry.place(x=500, y=65)

        self.generalToolsIpAddrButton = Button(self.generalToolsFrame, text="Get!", width=5, 
                                               command=lambda : self.getIpAddr(self.generalToolsIpAddrEntry.get()))
        self.generalToolsIpAddrButton.place(x=650, y=65)

        # Port Scan
        self.generalToolsPortScanTitleLabel = Label(self.generalToolsFrame, text="Port Scan", fg="#CFCFCF", 
                                            bg="#535353", font="bahnschrift 15 bold")
        self.generalToolsPortScanTitleLabel.place(x=50, y=120)

        self.generalToolsPortScanEntry = Entry(self.generalToolsFrame, width = 10, font="bahnschrift 15", fg="#ffffff", bg="#252525")
        self.generalToolsPortScanEntry.insert(0, "Target IP")
        self.generalToolsPortScanEntry.bind("<FocusIn>", self.on_click_portScan)
        self.generalToolsPortScanEntry.bind("<FocusOut>", self.on_leave_portScan)
        self.generalToolsPortScanEntry.place(x=500, y=120)

        # Create a Frame + Scrollbar for Port Scan Results
        self.terminalFrame = Frame(self.generalToolsFrame, width=665, height=525, background="#252525", highlightbackground="#ffffff", highlightthickness=2)
        self.terminalFrame.pack_propagate(False)
        self.terminalFrame.place(x = 50, y = 175)

        self.terminalScrollCanvas = Canvas(self.terminalFrame, background="#252525", highlightbackground="#ffffff", yscrollincrement=8)
        self.terminalScrollCanvas.pack(side = LEFT, fill = BOTH, expand = 1)
       
        self.terminalScrollbar = Scrollbar(self.terminalFrame, orient=VERTICAL, command = self.terminalScrollCanvas.yview)
        self.terminalScrollbar.pack(side = RIGHT, fill = Y)

        self.terminalScrollCanvas.configure(yscrollcommand=self.terminalScrollbar.set)
        self.terminalScrollCanvas.bind("<Configure>", lambda e : self.terminalScrollCanvas.configure(scrollregion=self.terminalScrollCanvas.bbox("all")))
        self.terminalScrollCanvas.bind_all("<MouseWheel>", lambda e : self.terminalScrollCanvas.yview_scroll(-1, "units"))

        self.terminalContentFrame = Frame(self.terminalScrollCanvas, background="#252525", highlightbackground="#ffffff")
        self.terminalScrollCanvas.create_window((0,0), window = self.terminalContentFrame, anchor = NW)
        self.terminalContentFrame.bind("<Configure>", lambda e : self.terminalScrollCanvas.configure(scrollregion=self.terminalScrollCanvas.bbox("all")))

        self.generalToolsPortScanButton = Button(self.generalToolsFrame, text="Scan!", width=5, 
                                               command=lambda : self.executePortScan(self.generalToolsPortScanEntry.get(), self.terminalContentFrame))
        self.generalToolsPortScanButton.place(x=650, y=120)

        self.homeTitleFrame.pack_propagate(0)
        self.homeTitleFrame.pack()
        self.projDetFrame.pack_propagate(0)
        self.projDetFrame.pack()
        self.howToUseFrame.pack_propagate(0)
        self.howToUseFrame.pack()
        self.generalToolsFrame.pack_propagate(0)
        self.generalToolsFrame.pack()

    def on_click_ipaddr(self, *args) :
        if(self.generalToolsIpAddrEntry.get() == "Interface") :
            self.generalToolsIpAddrEntry.delete(0, "end")
    
    def on_leave_ipaddr(self, *args) :
        if(self.generalToolsIpAddrEntry.get() == "") :
            self.generalToolsIpAddrEntry.insert(0, "Interface")

    def on_click_portScan(self, *args) :
        if(self.generalToolsPortScanEntry.get() == "Target IP") :
            self.generalToolsPortScanEntry.delete(0, "end")
    
    def on_leave_portScan(self, *args) :
        if(self.generalToolsPortScanEntry.get() == "") :
            self.generalToolsPortScanEntry.insert(0, "Target IP")

    def getIpAddr(self, interface) :
        self.ipAddress, interface = getIpAddress(interface)
        Footer.addIpAddr(self.ipAddress, interface)

    def executePortScan(self, targetIp, canvas) :
        portScanner(targetIp, canvas)
        