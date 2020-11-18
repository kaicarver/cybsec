#!/usr/bin/python3
import signal
from kamene.all import *

import socket, fcntl, struct

iface=b"ens33"
mask = socket.inet_ntoa(fcntl.ioctl(socket.socket(socket.AF_INET, socket.SOCK_DGRAM), 35099, struct.pack('256s', iface))[20:24])
print("subnet mask =", mask)

def keyboardInterruptHandler(signal, frame):
    print("KeyboardInterrupt (ID: {}). Au revoir !".format(signal))
    exit(0)

signal.signal(signal.SIGINT, keyboardInterruptHandler)

# boucle 254 adresses IP
for i in range(1, 255):
    ip = "192.168.99." + str(i)
    arpRequest = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip)
    arpResponse = srp1(arpRequest, timeout=.1, verbose=False)
    print(i, end=" ", flush=True)
    if arpResponse:
        print("\nIP: " + arpResponse.psrc + " MAC: " + arpResponse.hwsrc)
