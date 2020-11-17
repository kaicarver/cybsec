#!/usr/bin/python3
import socket,struct, binascii

rawsocket=socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))

#Capture d'un packet
pkt=rawsocket.recvfrom(2048)
#récupérer l'entete Ethernet
EnteteEth=pkt[0][0:14] #on prend les 14 premiers octets corressependant à l'entete Ethernet
#on va unpack le contenu
EnteteEthernet= struct.unpack("!6s6s2s",EnteteEth)# un tuple(dmac,smac,ethtype)
dmac=binascii.hexlify(EnteteEthernet[0]).decode()
smac=binascii.hexlify(EnteteEthernet[1]).decode()
ethtype=binascii.hexlify(EnteteEthernet[2]).decode()
print("Adresse Mac DST :{}\n Adresse Mac SRC : {}\n Ethernet Type:{}\n".format(dmac,smac,ethtype))

#récupérer l'entete IP
EnteteIP=EnteteEth=pkt[0][14:34] #On prend les 20 octets correspondant à l'entete IP
EntIP= struct.unpack("!12s4s4s",EnteteIP)
IPs=socket.inet_ntoa(EntIP[1])
IPd=socket.inet_ntoa(EntIP[2])
print("Adresse IP SRC :{}\n Adresse IP DST : {}\n".format(IPs,IPd))
EnteteTCP = pkt[0][34:54]
EntTCP= struct.unpack("!HH16s",EnteteTCP) #H unpack en int sur 2 octets (port_source,port_dest,reste)
print("N° PORT SRC :{}\n N° PORT DST : {}\n".format(EntTCP[0],EntTCP[1]))
