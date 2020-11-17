#!/usr/bin/python3
import socket,struct, binascii



rawsocket=socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))

rawsocket.bind(("ens33",socket.htons(0x0800)))

#encapsulation 
packet = struct.pack("6s6s2s" , b'\xaa\xaa\xaa\xaa\xaa\xaa',b'\xbb\xbb\xbb\xbb\xbb\xbb', b'\x08\x00')
rawsocket.send(packet + b'HELLO WORLD!')