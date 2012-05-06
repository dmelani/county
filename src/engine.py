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
		self.dude.percieve()
		self.done = False

	def run(self):
		self.dude.move(300.0, 100.0, 300.0)
		self.dude.look_at(600.0, 3.5, 0.0)
		while not self.done:
			#do everything
			self.handle_events()
			self.handle_queue()
			self.firmament.clear()
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
			event = data[0]
			params = data[1:]
			if event == 'add':
				self.terra.add(params[0])
			if event == 'randomize':
				self.terra.randomize()
	
	def handle_events(self):
		events = pygame.event.get()
		for event in events:
			if event.type == QUIT:
				self.done = True
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					self.done = True

