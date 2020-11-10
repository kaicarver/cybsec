#!/bin/bash

# script bash pour la gestion de user dans le système linux
# 1- afficher un menu pour l'utilisateur pour lui donner le choix de quelles sont les actions disponibles
# 2- avec case vous allez traiter chaque action choisi par l'utilisateur
# 3- les actions sont les suivantes:
# 	-créer un nouvel utilisateur
# 	-rechercher un user
# 	-supprimer un utilisateur
# 4- utiliser la boucle pour que le script reste toujours en execution jusqu'à que l'utilisateur tape la mot quitter

INPUT=""

while [ "$INPUT" != "q" ]; do
  echo "Commandes disponibles :"
  echo "1: créer un nouvel utilisateur"
	echo "2: rechercher un user"
	echo "3: supprimer un utilisateur"
	echo "q: quitter"
  read -n1 INPUT
  case "$INPUT" in
  1)
    Message="Creer"
    ;;
  2)
    Message="Rechercher"
    ;;
  3)
    Message="Supprimer"
    ;;
  q)
    Message="Au revoir !"
    ;;
  *)
    Message="$INPUT: commande inconnue"
    ;;
  esac
  echo
  echo $Message
done
