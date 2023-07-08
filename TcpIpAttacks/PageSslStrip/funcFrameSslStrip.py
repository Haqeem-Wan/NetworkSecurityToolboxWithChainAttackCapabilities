import threading
import traceback
import subprocess
import time
import signal

from tkinter import *

def startSslStrip(terminalContentFrame, wiresharkContentFrame, errorOutputContentFrame, colorConfig = "#252525") :
    global sslStripIsRunning, sslStripThreads, terminalLabel, wiresharkLabel, errorOutputLabel

    sslStripIsRunning = False
    sslStripThreads = threading.Thread(target = lambda : sslStripHub())

    terminalLabel = Label(terminalContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=480)
    wiresharkLabel = Label(wiresharkContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=480)
    errorOutputLabel = Label(errorOutputContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=480)
    terminalLabel.configure(bg = colorConfig) 
    wiresharkLabel.configure(bg = colorConfig)
    errorOutputLabel.configure(bg = colorConfig)

    terminalLabel["text"] += "$ Running SSL Strip Attack...\n\n"

    runSslStrip()

    terminalLabel.pack(anchor = NW)
    errorOutputLabel.pack(anchor = NW)

def stopSslStrip() :
    global sslStripThreads, sslStripIsRunning

    try:
        terminalLabel["text"] += "\n$ Stopping SSL Strip Attack...\n\n"
        sslStripIsrunning = False
        sslStripThreads.join(0)
        sslStripThreads = None

        process.send_signal(signal.SIGINT)
        process.wait()
        runTerminal1Thread.join(timeout=0.05)
        #runTerminal2Thread.join(timeout=0.05)

        terminalLabel["text"] += "$ SSL Strip Attack successfully stopped!\n"
    except (AttributeError, RuntimeError):
        errorOutputLabel["text"] += traceback.format_exc()
    except Exception as e:
        errorOutputLabel["text"] += "ERROR : \n" + e + "\n"

def runSslStrip() :
    global sslStripThreads, sslStripIsRunning
    sslStripIsRunning = True
    sslStripThreads.start()

def sslStripHub():
    global process, runTerminal1Thread
    #process = subprocess.Popen(["echo", "1", ">", "/proc/sys/net/ipv4/ip_forward"], stdin = subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #process.stdin.write(f"iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 8080".encode())
    process = subprocess.Popen(["echo", "kali"], stdin = subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    runTerminal1Thread = threading.Thread(target=reader, args=(process,))
    runTerminal1Thread.start()

    commands = ["echo linux"]

    for command in commands:
        print("CHECK 1")
        terminalLabel["text"] += f"Executing command : {command}"
        process.stdin.write(f"{command}\n".encode())
        #process.stdin.flush()
        print("CHECK 2")
        # Give it some time to process the command and generate output
        time.sleep(2)
        print("CHECK 3")

    # process.stdin.write(f"echo linux".encode())

    # SOLVE HOW TO RUN MULTIPLE POPEN AND STILL BE ABLE TO CALL SIGINT

def reader(proc):
    print(output + " 1")
    while True:
        output = proc.stdout.readline().decode()
        print(output + " 2")
        if output == '' and proc.poll() is not None:
            break
        if output:
            print(output.strip())