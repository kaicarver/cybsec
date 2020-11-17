#!/usr/bin/python3
from kamene.all import *
import threading

def scan1port(ip, port):
    scan = sr1(IP(dst=ip)/TCP(dport=port, flags="S"), verbose=False, timeout=.2)
    if scan:
        if scan[TCP].flags == 18:
            print("port {} ouvert!".format(port))
        else:
            #print("port {} echange inconnu 0x{}".format(port, hex(scan[TCP].flags)))
            pass
    else:
        print("port {} ferme !".format(port))

ip = sys.argv[1]
max = int(sys.argv[2])
use_threads = True

print("port {} scan {} ports, use threads {}".format(ip, max, use_threads))
for port in range(max):
    if use_threads:
        x = threading.Thread(target=scan1port, args=(ip, port,))
        x.start()
    else:
        scan1port(ip, port)
