import scapy.all as scapy
import time
import threading
import traceback

import subprocess
import random

from tkinter import *

def startMac(terminalContentFrame, errorOutputContentFrame, colorConfig = "#252525") :
    global macThreads, terminalLabel, errorOutputLabel

    macThreads = threading.Thread(target = lambda : spoof_mac_address())

    terminalLabel = Label(terminalContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=480)
    errorOutputLabel = Label(errorOutputContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=480)
    terminalLabel.configure(bg = colorConfig) 
    errorOutputLabel.configure(bg = colorConfig)

    terminalLabel["text"] += "$ Running MAC Spoofing Attack...\n\n"
    #terminalLabel["text"] += "\n$ Test 12345678910.11.12.13.14.15.16.17.18.19.20.21.22.23.24.25.26.27.28.29.30.31.32.33.34.35.36.37.38.39.40\n"

    runMacSpoofAttack()

    terminalLabel.pack(anchor = NW)
    errorOutputLabel.pack(anchor = NW)

def stopMac() :
    global macThreads
    stopMacThreads = threading.Thread(target = lambda : revert_mac_address(terminalLabel))

    try:
        terminalLabel["text"] += "\n$ Stopping MAC Spoofing Attack...\n\n"
        macIsrunning = False
        macThreads.join(0)
        macThreads = None

        stopMacThreads.start()

        terminalLabel["text"] += "$ MAC Spoofing Attack successfully stopped!\n"
    except (AttributeError, RuntimeError):
        errorOutputLabel["text"] += traceback.format_exc()
    except Exception as e:
        errorOutputLabel["text"] += "ERROR : \n" + str(e) + "\n"

def stopMacChain(chainTerminalContentFrame, chainErrorContentFrame) :
    chainTerminalLabel = Label(chainTerminalContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=278)
    chainErrorOutputLabel = Label(chainErrorContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=278)

    chainStopMacThreads = threading.Thread(target = lambda : revert_mac_address(chainTerminalLabel))

    chainTerminalLabel.pack(anchor = NW)
    chainErrorOutputLabel.pack(anchor = NW)

    try:
        chainTerminalLabel["text"] += "\n$ Stopping MAC Spoofing Attack...\n\n"

        chainStopMacThreads.start()

        chainTerminalLabel["text"] += "$ MAC Spoofing Attack successfully stopped!\n"
        
        chainStopMacThreads.join(0)
        chainStopMacThreads = None
    except (AttributeError, RuntimeError):
        chainErrorOutputLabel["text"] += traceback.format_exc()
    except Exception as e:
        chainErrorOutputLabel["text"] += "ERROR : \n" + str(e) + "\n"

def runMacSpoofAttack() :
    global macThreads
    macThreads.start()

def spoof_mac_address():
    # Get the current MAC address of the "eth0"
    terminalLabel["text"] += "$ Old MAC Address : " + get_current_mac_address() +"\n"

    # Change the MAC address of the "eth0"
    subprocess.call(["ifconfig", "eth0", "down"])
    subprocess.call(["macchanger", "-r", "eth0"])
    subprocess.call(["ifconfig", "eth0", "up"])

    terminalLabel["text"] += "$ New MAC Address : " + get_current_mac_address() +"\n"

def revert_mac_address(terminalLabel) :
    
    terminalLabel["text"] += "$ Old MAC Address : " + get_current_mac_address() +"\n"

    # Change the MAC address of the "eth0"
    subprocess.call(["ifconfig", "eth0", "down"])
    subprocess.call(["macchanger", "-p", "eth0"])
    subprocess.call(["ifconfig", "eth0", "up"])

    terminalLabel["text"] += "$ New MAC Address : " + get_current_mac_address() +"\n"

def get_current_mac_address():
    output = subprocess.run(['ip', 'link', 'show', 'dev', "eth0"], capture_output=True, text=True)
    for line in output.stdout.split('\n'):
        if 'link/ether' in line:
            mac_address = line.split()
            return mac_address[1]
    return None
