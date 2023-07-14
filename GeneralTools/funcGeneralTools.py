import netifaces as ni
import subprocess
from tkinter import *

def getIpAddress(interface) :
    try :
        ipAddr = ni.ifaddresses(interface)[ni.AF_INET][0]['addr']
    except Exception as e:
        ipAddr = "Interface Not Found / Running!  "
        interface = "{Not Found}"
    return ipAddr, interface

def portScanner(targetIp, frame) :
    process = subprocess.Popen(["nmap", targetIp], stdin=subprocess.PIPE, 
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    stdout, stderr = process.communicate()

    output = stdout.decode()

    portScanLabel = Label(frame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 12", justify = "left", wraplength=480)

    for line in output.splitlines() :
        portScanLabel["text"] += line + "\n"
    
    portScanLabel.pack(anchor=NW)