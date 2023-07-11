import threading
import traceback

from tkinter import *

def startHttpSessionHijacking(terminalContentFrame, wiresharkContentFrame, errorOutputContentFrame, colorConfig = "#252525") :
    global httpSessionHijackingIsRunning, httpSessionHijackingThreads, terminalLabel, wiresharkLabel, errorOutputLabel

    httpSessionHijackingIsRunning = False
    httpSessionHijackingThreads = threading.Thread(target = lambda : executeHttpHijack())

    terminalLabel = Label(terminalContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=480)
    wiresharkLabel = Label(wiresharkContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=480)
    errorOutputLabel = Label(errorOutputContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=480)
    terminalLabel.configure(bg = colorConfig) 
    wiresharkLabel.configure(bg = colorConfig)
    errorOutputLabel.configure(bg = colorConfig)

    terminalLabel["text"] += "$ Running HTTP Session Hijacking...\n\n"

    runHttpSessionHijacking()

    terminalLabel.pack(anchor = NW)
    errorOutputLabel.pack(anchor = NW)

def stopHttpSessionHijacking() :
    global httpSessionHijackingThreads, httpSessionHijackingIsRunning

    try:
        terminalLabel["text"] += "\n$ Stopping aATTACK...\n\n"
        httpSessionHijackingIsrunning = False
        httpSessionHijackingThreads.join(0)
        httpSessionHijackingThreads = None

        terminalLabel["text"] += "$ aATTACK successfully stopped!\n"
    except (AttributeError, RuntimeError):
        errorOutputLabel["text"] += traceback.format_exc()
    except Exception as e:
        errorOutputLabel["text"] += "ERROR : \n" + e + "\n"

def runHttpSessionHijacking() :
    global httpSessionHijackingThreads, httpSessionHijackingIsRunning
    httpSessionHijackingIsRunning = True
    httpSessionHijackingThreads.start()

def executeHttpHijack():
    # Add attack code
    pass