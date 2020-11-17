# En-tete IP v4

Un paquet IP est constitue de deux sections, une en-tete et des donnees.

L'en-tete contient 14 champs, dont 13 obligatoires, et le champ _options_.

20 octets sans compter les options.

Note: le packet IP est souvent contenu dans un truc Ethernet (connexion cable paire torsadee, Wi-Fi) dont l'en-tete fait 14 octets.

## Version

4 bits. Le numero de version. Pour IPv4 egale toujours 4.

## IHL - Internet Heder Length

4 bits. Contient la taille de l'en-tete IPv4 en vords de 32 bits. Valeur minimale de 5, donc 5 x 32 octets. L'en-tete IPv4 est de taille variable selon les options. 

## DSCP - Differentiated Services Code Point

6 bits. Specifie type de service, genre VoIP.

## ECN - Explicit Congestion Notification

2 bits. Utilise en option pour indiquer reseau avec trop de trafic.

## Total Length

16 bits. Taille totale du packet en octets, en-tete plus donnees. Minimum 20.

## Identification

16 bits. Identifie fragments de datagram.

## Flags

3 bits. Pour controler les fragments. 0, DF (don't fragment), MF (more fragment).

## Fragment Offset

13 bits. Offset du fragment en blocs de 8 bits.

## TTL - Time To Live

pour la partie donnees du datagramme.
8 bits. Pour empecher les boucles.

valeurs : Linux 64, Windows 128, Cisco 255

## Protocol

Protocole utilise pour la partie donnees du datagramme.

## Header Checksum

Checksum de l'en-tete.

## Source address

Adresse envoyeur du paquet.

## Destination address

Adresse destinataire du paquet.

## Options

Pas utilise souvent.

[A completer]
