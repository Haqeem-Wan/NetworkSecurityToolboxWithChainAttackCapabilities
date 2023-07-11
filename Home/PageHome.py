from tkinter import *
from tkinter.ttk import Separator

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
        self.homeTitleLabel.place(x=525, y=20)
        
        # Project Details Frame
        self.projDetFrame = Frame(self.homeScrollFrame, width=1280, height=385,
                                         background="#383838", borderwidth=2, relief="groove")
        
        self.projDetTitleLabel = Label(self.projDetFrame, text="PROJECT DETAILS", fg="#CFCFCF", 
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
        self.howToUseFrame = Frame(self.homeScrollFrame, width=1280, height=600,
                                         background="#444444", borderwidth=2, relief="groove")
        
        self.howToUseTitleLabel = Label(self.howToUseFrame, text="HOW TO USE", fg="#CFCFCF", 
                                        bg="#444444", font="bahnschrift 15 bold")
        self.howToUseTitleLabel.place(x=10, y=10)

        self.howToUseSeparator = Separator(self.howToUseFrame, orient="horizontal")
        self.howToUseSeparator.place(y=45, relwidth=1)
    
        self.homeTitleFrame.pack_propagate(0)
        self.homeTitleFrame.pack()
        self.projDetFrame.pack_propagate(0)
        self.projDetFrame.pack()
        self.howToUseFrame.pack_propagate(0)
        self.howToUseFrame.pack()
