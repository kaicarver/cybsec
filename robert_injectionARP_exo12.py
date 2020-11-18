#!/usr/bin/python3
import socket,struct, ipaddress

#ethertype = 0x0800  # IPv4
ethertype = 0x0806  # ARP

rawsocket=socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(ethertype))
rawsocket.bind(("ens33",socket.htons(ethertype)))

def format_ip(ip):
    # retourne l'IP ecrit en hexa sous 4 octets
    return int(ipaddress.IPv4Address(ip))

#encapsulation 
src_mac = b"\x00\x0c\x29\x69\x12\x19"
ip_dst_mac = b"\xff"*6
ether_type = b"\x08\x06"
#en-tete ARP, voir http://frameip.com/entete-arp/
# arp_type, ptype, hlen, plen, op, src_ip, src_mac
packet = struct.pack("6s6s2s" , b'\xaa\xaa\xaa\xaa\xaa\xaa',b'\xbb\xbb\xbb\xbb\xbb\xbb', b'\x08\x00')
rawsocket.send(packet + b'HELLO WORLD!')