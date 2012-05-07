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
		x,y = self.firmament.modes[0]
		aspect = float(x)/float(y)
		self.dude = dude.Dude(aspect)
		self.done = False

	def run(self):
		self.dude.move_to(600.0, 100.0, 300.0)
		self.dude.look_at(600.0, 100.0, 0.0)
		while not self.done:
			#do everything
			self.handle_events()
			self.handle_queue()
			self.firmament.clear()
			self.dude.perceive()
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
			print 'Engine received:', data
			event = data[0]
			params = data[1:]
			if event == 'add':
				self.terra.add(params[0])
			if event == 'randomize':
				self.terra.randomize()
			if event == 'move_to':
				self.dude.move_to(params[0], params[1], params[2])
			if event == 'look_at':
				self.dude.look_at(params[0], params[1], params[2])
	
	def handle_events(self):
		events = pygame.event.get()
		for event in events:
			if event.type == QUIT:
				self.done = True
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					self.done = True

