#!/usr/bin/python
import sys,os

def processus_enfant():
  print("je suis enfant, pid ", os.getpid())

def processus_parent():
  print("je suis parent, pid ", os.getpid())
  pidenfant = os.fork()
  if pidenfant == 0:
    processus_enfant()
  else:
    print("id enfant ", pidenfant)

processus_parent()
