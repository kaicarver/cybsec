#!/bin/bash

# Script bash pour la gestion de user dans le système linux

# Pour l'instant c'est juste un menu...

searchuser () {
  echo
  read -p "Utilisateur: " USER
  echo
  REP=$(grep $USER /etc/passwd | cut -d: -f6)
  if test -d "$REP"; then
    echo L\'utilisateur $USER existe ici: $REP
  else
    echo Utilisateur $USER introuvable
  fi
}

input=""

while [ "$input" != "q" ]; do
  echo "Commandes disponibles :"
  echo "1: créer un nouvel utilisateur"
	echo "2: rechercher un utilisateur"
	echo "3: supprimer un utilisateur"
	echo "q: quitter"
  read -n1 input
  case "$input" in
  1)
    message="Creer"
    ;;
  2)
    message="Rechercher"
    searchuser
    ;;
  3)
    message="Supprimer"
    ;;
  q)
    message="Au revoir !"
    ;;
  *)
    message="$input: commande inconnue"
    ;;
  esac
  echo
  echo $message
done
