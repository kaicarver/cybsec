#!/usr/bin/python3
import socketserver

# Modification de la classe BaseRequestHandler

def dowrite(text):
    fh = open("socklog.txt", "a")
    fh.write(text)
    fh.close()

class EchoServeur(socketserver.BaseRequestHandler):
    def handle(self):
        print("[*]Connexion depuis :", self.client_address)
        data = "rien"
        # Boucle qui renvoie ce que le client envoie et s'arrete s'il ne recois rien
        while len(data):
            data = self.request.recv(1024)
            print("[*]Le client envoie :", data.decode().strip())
            dowrite(data.decode())
            self.request.send(data)
        print("[-]Déconnexion du client :",self.client_address)

infosrv=("0.0.0.0",8080)
srv = socketserver.ThreadingTCPServer(infosrv,EchoServeur)
try:
    srv.serve_forever()
except KeyboardInterrupt:
    print("au revoir!")
