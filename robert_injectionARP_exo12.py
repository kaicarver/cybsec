#!/usr/bin/python3
import socket,struct, binascii

#ethertype = 0x0800  # IPv4
ethertype = 0x0806  # ARP

rawsocket=socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))

rawsocket.bind(("ens33",socket.htons(ethertype)))

#encapsulation 
packet = struct.pack("6s6s2s" , b'\xaa\xaa\xaa\xaa\xaa\xaa',b'\xbb\xbb\xbb\xbb\xbb\xbb', b'\x08\x00')
rawsocket.send(packet + b'HELLO WORLD!')