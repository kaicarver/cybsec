#!/usr/bin/python
import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind(("0.0.0.0", 8080))
sock.listen(2)

print("Attente connexion depuis un client...")

(client, (ip, port)) = sock.accept()
print("Connexion depuis l'IP : ", ip)

# echo
data = b'non nul'
while len(data):
  data = client.recv(2048)
  str = data.decode("utf-8")
  print("Message du client : ", str)
  client.send(data)

print("Fermeture connexion.")
client.close()
