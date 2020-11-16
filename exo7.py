#!/usr/bin/python
import sys,os
file = sys.argv[1]
try:
  statfichier = os.stat(file)
  if statfichier:
    print("nom du fichier: " + file)
  else:
    print("no stat for: ", file)
except Exception as e:
  print("Exception!", e)
