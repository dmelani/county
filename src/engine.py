import pygame
from pygame.locals import *
import Queue
import time
import sys
import firmament
import terra
import dude

class Engine(object):
	def __init__(self, me_q):
		print 'Engine starting...'
		self.me_q = me_q
		self.firmament = firmament.Firmament()
		self.terra = terra.Terra()
		self.dude = dude.Dude()
		self.dude.move(10.0, 1.0, 10.0)
		self.dude.look_at(0.0, 0.0, 0.0)
		self.done = False

	def run(self):
		while not self.done:
			#do everything
			self.handle_events()
			self.handle_queue()
			self.firmament.clear()
			self.dude.percieve()
			self.terra.the_lone_range_rides_again()
			pygame.display.flip()
		print "Engine stopping..."
		pygame.quit()
	
	def handle_queue(self):
		try:
			data = self.me_q.get_nowait()
		except Queue.Empty:
			pass
		else:
			event, param = data
			if event == 'add':
				self.terra.add(param)

	def handle_events(self):
		events = pygame.event.get()
		for event in events:
			if event.type == QUIT:
				self.done = True

