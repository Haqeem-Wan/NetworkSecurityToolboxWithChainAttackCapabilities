from tkinter import *

class Footer:
    def __init__ (self, root, footerFrame):
        global footerFrameSet, ipAddressLabel
        self.root = root
        footerFrameSet = footerFrame
        ipAddressLabel = Label(footerFrameSet, text="", font="bahnschrift 15", fg="#CFCFCF", bg="#333333")
        ipAddressLabel.pack(side=RIGHT)

    def addIpAddr(ipAddress, interface) :
        ipAddressLabel.config(text="IP " + interface + " : " + ipAddress)