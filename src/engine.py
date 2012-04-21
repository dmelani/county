import firmament
import pygame
import time

class Engine(object):
	def __init__(self, me_q):
		print 'Engine starting...'
		self.me_q = me_q
		self.firmament = firmament.Firmament()
		self.done = False

	def run(self):
		while not self.done:
			#do everything
			#self.handle_events()
			pygame.display.flip()
"""	
	def handle_events(self):
		events = pygame.event.get()
		for event in events:
			if event.type == QUIT  or event.type == KEYDOWN and event.key == K_ESCAPE:
				self.done = True
"""
