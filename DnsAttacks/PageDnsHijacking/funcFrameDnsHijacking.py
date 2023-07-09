import scapy.all as scapy
import threading
import traceback

from tkinter import *

def startDnsHijacking(terminalContentFrame, wiresharkContentFrame, errorOutputContentFrame, colorConfig = "#252525") :
    global dnsHijackingIsRunning, dnsHijackingThreads, terminalLabel, wiresharkLabel, errorOutputLabel

    dnsHijackingIsRunning = False
    dnsHijackingThreads = threading.Thread(target = lambda : dnsHijackingHub())

    terminalLabel = Label(terminalContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=480)
    wiresharkLabel = Label(wiresharkContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=480)
    errorOutputLabel = Label(errorOutputContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=480)
    terminalLabel.configure(bg = colorConfig) 
    wiresharkLabel.configure(bg = colorConfig)
    errorOutputLabel.configure(bg = colorConfig)

    terminalLabel["text"] += "$ Running DNS Hijacking Attack...\n\n"

    runDnsHijacking()

    terminalLabel.pack(anchor = NW)
    errorOutputLabel.pack(anchor = NW)

def stopDnsHijacking() :
    global dnsHijackingThreads, dnsHijackingIsRunning

    try:
        terminalLabel["text"] += "\n$ Stopping DNS Hijacking Attack...\n\n"
        dnsHijackingIsrunning = False
        dnsHijackingThreads.join(0)
        dnsHijackingThreads = None

        terminalLabel["text"] += "$ DNS Hijacking Attack successfully stopped!\n"
    except (AttributeError, RuntimeError):
        errorOutputLabel["text"] += traceback.format_exc()
    except Exception as e:
        errorOutputLabel["text"] += "ERROR : \n" + e + "\n"

def runDnsHijacking() :
    global dnsHijackingThreads, dnsHijackingIsRunning
    dnsHijackingIsRunning = True
    dnsHijackingThreads.start()

def dnsHijackingHub():
    # Add attack code
    pass