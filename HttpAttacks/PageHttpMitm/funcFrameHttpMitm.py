import threading
import traceback
import subprocess
import re
import signal

from tkinter import *

def startHttpMitm(interface, terminalContentFrame, wiresharkContentFrame, errorOutputContentFrame, colorConfig = "#252525") :
    global httpMitmIsRunning, httpMitmThreads, terminalLabel, wiresharkLabel, errorOutputLabel

    httpMitmIsRunning = False
    httpMitmThreads = threading.Thread(target = lambda : executeHttpMitm(interface))

    terminalLabel = Label(terminalContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=480)
    wiresharkLabel = Label(wiresharkContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=480)
    errorOutputLabel = Label(errorOutputContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=480)
    terminalLabel.configure(bg = colorConfig) 
    wiresharkLabel.configure(bg = colorConfig)
    errorOutputLabel.configure(bg = colorConfig)

    terminalLabel["text"] += "$ Running HTTP Man-In-The-Middle Attack...\n\n"

    runHttpMitm()

    terminalLabel.pack(anchor = NW)
    errorOutputLabel.pack(anchor = NW)

def stopHttpMitm() :
    global httpMitmThreads, httpMitmIsRunning, errorOutputLabel

    try:
        terminalLabel["text"] += "\n$ Stopping HTTP Man-In-The-Middle Attack...\n\n"
        httpMitmIsrunning = False
        httpMitmThreads.join(0)
        httpMitmThreads = None

        ferretMitmProcess.send_signal(signal.SIGINT)
        ferretMitmThread.join(0)

        terminalLabel["text"] += "$ HTTP Man-In-The-Middle Attack successfully stopped!\n"
    except (AttributeError, RuntimeError):
        errorOutputLabel["text"] += traceback.format_exc()
    except Exception as e:
        errorOutputLabel["text"] += "ERROR : \n" + str(e) + "\n"

def runHttpMitm() :
    global httpMitmThreads, httpMitmIsRunning
    httpMitmIsRunning = True
    httpMitmThreads.start()

def executeHttpMitm(interface):
    global ferretMitmProcess, ferretMitmThread

    ferretMitmProcess = subprocess.Popen(["ferret-sidejack", "-i", interface], 
                                         stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    ferretMitmThread = threading.Thread(target=reader, args=(ferretMitmProcess,))
    ferretMitmThread.start()

def reader(proc):
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    while True:
        output = proc.stdout.readline().decode('utf8', errors='strict')
        if output == '' and proc.poll() is not None:
            break
        if output:
            ansiStripOutput = ansi_escape.sub('', output)
            terminalLabel["text"] += "$ " + ansiStripOutput.strip() + "\n"

def arpErrorHandling(error) :
    errorOutputLabel["text"] += str(error) + "\n"
