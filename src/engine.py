import pygame
from pygame.locals import *
import time
import sys
import firmament
import terra

class Engine(object):
	def __init__(self, me_q):
		print 'Engine starting...'
		self.me_q = me_q
		self.firmament = firmament.Firmament()
		self.terra = terra.Terra()
		self.done = False

	def run(self):
		while not self.done:
			#do everything
			self.firmament.clear()
			self.terra.the_lone_range_rides_again()
			self.handle_events()
			pygame.display.flip()
		print "Engine stopping..."
		pygame.quit()

	def handle_events(self):
		events = pygame.event.get()
		for event in events:
			if event.type == QUIT:
				self.done = True

