#!/usr/bin/python3
import sys, urllib.request

class Disallowpresent(Exception):
  def __init__(self, chemin):
    self.chemin_desactiver = chemin
  def __str__(self):
      return repr(self.chemin_desactiver)

robots = urllib.request.urlopen(sys.argv[1])

for ligne in robots.readlines():
  try:
    lignestr = ligne.decode()
    if b'disallow' in ligne.lower():
      print(lignestr)
      raise Disallowpresent(lignestr.strip("Disallow: "))
  except Disallowpresent as ex:
    print("Exception pour le chemin {}".format(ex.chemin_desactiver))
