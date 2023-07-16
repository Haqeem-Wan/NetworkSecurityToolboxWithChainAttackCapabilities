import threading
import traceback
import subprocess
import re
import signal

from tkinter import *

def startHttpMitm(interface, terminalContentFrame, errorOutputContentFrame, colorConfig = "#252525") :
    global httpMitmIsRunning, httpMitmThreads, terminalLabel, errorOutputLabel

    httpMitmIsRunning = False
    httpMitmThreads = threading.Thread(target = lambda : executeHttpMitm(interface))

    terminalLabel = Label(terminalContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=480)
    errorOutputLabel = Label(errorOutputContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=480)
    terminalLabel.configure(bg = colorConfig) 
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
    ferretMitmThread = threading.Thread(target=reader, args=(ferretMitmProcess,terminalLabel,))
    ferretMitmThread.start()

def reader(proc, terminalLabel):
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    while True:
        output = proc.stdout.readline().decode('utf8', errors='strict')
        if output == '' and proc.poll() is not None:
            break
        if output:
            ansiStripOutput = ansi_escape.sub('', output)
            terminalLabel["text"] += "$ " + ansiStripOutput.strip() + "\n"

def startHttpMitmChain(queue, interface, terminalContentFrame, errorOutputContentFrame) :
    terminalLabel = Label(terminalContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=278)
    errorOutputLabel = Label(errorOutputContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=278)
    terminalLabel.pack(anchor = NW)
    errorOutputLabel.pack(anchor = NW)

    terminalLabel["text"] += "$ Running HTTP Man-In-The-Middle Attack...\n\n"

    try :
        ferretMitmProcess = subprocess.Popen(["ferret-sidejack", "-i", interface], 
                                            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        ferretMitmThread = threading.Thread(target=reader, args=(ferretMitmProcess,terminalLabel,))
        ferretMitmThread.start()

        queue.put((ferretMitmProcess, ferretMitmThread))
    except Exception as e :
        errorOutputLabel["text"] += "ERROR : \n" + str(e) + "\n"

def stopHttpMitmChain(chainTerminalContentFrame, chainErrorContentFrame) :
    chainTerminalLabel = Label(chainTerminalContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=278)
    chainErrorOutputLabel = Label(chainErrorContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=278)
    chainTerminalLabel.pack(anchor = NW)
    chainErrorOutputLabel.pack(anchor = NW)

    try:
        chainTerminalLabel["text"] += "\n$ Stopping HTTP Man-In-The-Middle Attack...\n\n"
        chainTerminalLabel["text"] += "$ HTTP Man-In-The-Middle Attack successfully stopped!\n"
    except (AttributeError, RuntimeError):
        chainErrorOutputLabel["text"] += traceback.format_exc()
    except Exception as e:
        chainErrorOutputLabel["text"] += "ERROR : \n" + str(e) + "\n"