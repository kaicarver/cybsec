#!/usr/bin/python
import _thread
import time

def travail_parallele(id):
  print("programme en parallele avec ID = {} en cours ...".format(id))
  compteur = 1
  while True:
    print("programme en parallele avec ID = {} compteur {}".format(id, compteur))
    time.sleep(2)
    compteur += 1

for i in range(5):
  _thread.start_new_thread(travail_parallele, (i,))

print("boucle infinie")

while True:
  pass
