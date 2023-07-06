import scapy.all as scapy
import threading
import traceback

from tkinter import *

def startdEvilTwinAttack(terminalContentFrame, wiresharkContentFrame, errorOutputContentFrame, colorConfig = "#252525") :
    global evilTwinAttackIsRunning, evilTwinAttackThreads, terminalLabel, wiresharkLabel, errorOutputLabel

    evilTwinAttackIsRunning = False
    evilTwinAttackThreads = threading.Thread(target = lambda : launchEvilTwin())

    terminalLabel = Label(terminalContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=480)
    wiresharkLabel = Label(wiresharkContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=480)
    errorOutputLabel = Label(errorOutputContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=480)
    terminalLabel.configure(bg = colorConfig) 
    wiresharkLabel.configure(bg = colorConfig)
    errorOutputLabel.configure(bg = colorConfig)

    terminalLabel["text"] += "$ Running Evil Twin Attack...\n\n"

    rundEvilTwinAttack()

    terminalLabel.pack(anchor = NW)
    errorOutputLabel.pack(anchor = NW)

def stopdEvilTwinAttack() :
    global evilTwinAttackThreads, evilTwinAttackIsRunning

    try:
        terminalLabel["text"] += "\n$ Stopping Evil Twin Attack...\n\n"
        evilTwinAttackIsrunning = False
        evilTwinAttackThreads.join(0)
        evilTwinAttackThreads = None

        terminalLabel["text"] += "$ Evil Twin Attack successfully stopped!\n"
    except (AttributeError, RuntimeError):
        errorOutputLabel["text"] += traceback.format_exc()
    except Exception as e:
        errorOutputLabel["text"] += "ERROR : \n" + e + "\n"

def rundEvilTwinAttack() :
    global evilTwinAttackThreads, evilTwinAttackIsRunning
    evilTwinAttackIsRunning = True
    evilTwinAttackThreads.start()

def launchEvilTwin():
    # Add attack code
    pass