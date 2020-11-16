#!/usr/bin/python
import threading
import queue
import time

class fil_de_travail(threading.Thread):
  def __init__(self, queue):
    threading.Thread.__init__(self)
    self.queue = queue
  def run(self):
    print("Dans fil de travail")
    while (True):
      compteur = self.queue.get()
      print("Je dors %d sec!"%compteur)
      time.sleep(compteur)
      self.queue.task_done()

queue = queue.Queue()


