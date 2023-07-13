from tkinter import *

class Footer:
    def __init__ (self, root, footerFrame):
        global footerFrameSet
        self.root = root
        footerFrameSet = footerFrame

    def addIpAddr(ipAddress) :
        ipAddressLabel = Label(footerFrameSet, text="IP : "+ipAddress, font="bahnschrift 15", fg="#CFCFCF", bg="#333333")
        ipAddressLabel.pack(side=RIGHT)