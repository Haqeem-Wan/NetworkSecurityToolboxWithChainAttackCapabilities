import scapy.all as scapy
import threading
import traceback

from tkinter import *

def startbATTACK(terminalContentFrame, wiresharkContentFrame, errorOutputContentFrame, colorConfig = "#252525") :
    global cATTACKIsRunning, cATTACKThreads, terminalLabel, wiresharkLabel, errorOutputLabel

    cATTACKIsRunning = False
    cATTACKThreads = threading.Thread(target = lambda : dATTACK())

    terminalLabel = Label(terminalContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=480)
    wiresharkLabel = Label(wiresharkContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=480)
    errorOutputLabel = Label(errorOutputContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=480)
    terminalLabel.configure(bg = colorConfig) 
    wiresharkLabel.configure(bg = colorConfig)
    errorOutputLabel.configure(bg = colorConfig)

    terminalLabel["text"] += "$ Running aATTACK...\n\n"

    runbATTACK()

    terminalLabel.pack(anchor = NW)
    errorOutputLabel.pack(anchor = NW)

def stopbATTACK() :
    global cATTACKThreads, cATTACKIsRunning

    try:
        terminalLabel["text"] += "\n$ Stopping aATTACK...\n\n"
        cATTACKIsrunning = False
        cATTACKThreads.join(0)
        cATTACKThreads = None

        terminalLabel["text"] += "$ aATTACK successfully stopped!\n"
    except (AttributeError, RuntimeError):
        errorOutputLabel["text"] += traceback.format_exc()
    except Exception as e:
        errorOutputLabel["text"] += "ERROR : \n" + e + "\n"

def runbATTACK() :
    global cATTACKThreads, cATTACKIsRunning
    cATTACKIsRunning = True
    cATTACKThreads.start()

def dATTACK():
    # Add attack code
    pass