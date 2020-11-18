#!/usr/bin/python3
import signal
from kamene.all import *

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
