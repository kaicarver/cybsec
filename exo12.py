#!/usr/bin/python3
import socket,struct, ipaddress

interface="ens33"
rawsocket=socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0806))
rawsocket.bind(("ens33",socket.htons(0x0800)))

def format_ip(ip):
	#la fonction qui return l'IP ecrit en hexa sous 4octet
	return ipaddress.IPv4Address(ip).packed

#encapsulation pour l'entete Ethernet
ip_src_mac = b"\x00\x0c\x29\xfc\x69\x9b"
ip_dst_mac = b"\xff"*6
ether_type = b"\x08\x06"

#entete ARP 
arp_type = b'\x00\x01'
arp_ptype = b'\x08\x00'
arp_hlen = b'\x06'
arp_plen = b'\x04'
arp_op = b'\x00\x01'
arp_src_ip = '192.168.99.129'
arp_dst_mac = b'\x00\x00\x00\x00\x00\x00'
arp_dst_ip = '192.168.99.2' # voir la doc dans le site www.frameip.com

arp_s_ip=format_ip(arp_src_ip)
arp_d_ip=format_ip(arp_dst_ip)

# construction de la trame 
#partie entete Ethernet
enteteETH = struct.pack("!6s6s2s" ,ip_src_mac,ip_dst_mac,ether_type)
#partie ARP
enteteARP = struct.pack("!2s2s1s1s2s6s4s6s4s" ,arp_type,arp_ptype,arp_hlen,arp_plen,arp_op,ip_src_mac,arp_s_ip,arp_dst_mac,arp_d_ip)
trameARP=enteteETH+enteteARP
rawsocket.send(trameARP)
#tester ce script et vérifier avec la commande tcpdump -i ens33 -v -XX