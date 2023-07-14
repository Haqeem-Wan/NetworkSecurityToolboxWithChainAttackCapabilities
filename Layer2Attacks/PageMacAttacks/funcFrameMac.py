import scapy.all as scapy
import time
import threading
import traceback

import subprocess
import random

from tkinter import *

def startMac(terminalContentFrame, errorOutputContentFrame, colorConfig = "#252525") :
    global macIsRunning, macThreads, terminalLabel, errorOutputLabel

    macIsRunning = False
    macThreads = threading.Thread(target = lambda : spoof_mac_address())

    terminalLabel = Label(terminalContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=480)
    errorOutputLabel = Label(errorOutputContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=480)
    terminalLabel.configure(bg = colorConfig) 
    errorOutputLabel.configure(bg = colorConfig)

    terminalLabel["text"] += "$ Running MAC Spoofing Attack...\n\n"

    runMacSpoofAttack()

    terminalLabel.pack(anchor = NW)
    errorOutputLabel.pack(anchor = NW)

def stopMac() :
    global macThreads, macIsRunning
    stopMacThreads = threading.Thread(target = lambda : revert_mac_address())

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

def runMacSpoofAttack() :
    global macThreads, macIsRunning
    macIsRunning = True
    macThreads.start()

def spoof_mac_address():
    # Get the current MAC address of the "eth0"
    terminalLabel["text"] += "$ Old MAC Address : " + get_current_mac_address() +"\n"

    # Change the MAC address of the "eth0"
    subprocess.call(["ifconfig", "eth0", "down"])
    subprocess.call(["macchanger", "-r", "eth0"])
    subprocess.call(["ifconfig", "eth0", "up"])

    terminalLabel["text"] += "$ New MAC Address : " + get_current_mac_address() +"\n"

def revert_mac_address() :
    
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
