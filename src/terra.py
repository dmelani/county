from OpenGL.GL import * 
from OpenGL.GLU import * 
from OpenGL.GLUT import * 
import time
import datetime
import histogram

class Terra(object):
	def __init__(self):
		self.timestamp = time.time()
		self.entities = []
		self.histogram = histogram.Histogram()
		self.entities.append(self.histogram)
		self.current_day = datetime.datetime.now().day

	def add(self, amount):
		self.histogram.add(amount)
	
	def randomize(self):
		self.histogram.randomize()	

	def revolve(self):
		now = time.time()
		delta = now - self.timestamp
		current_day = datetime.datetime.now().day

		if current_day > self.current_day:
			self.histogram.advance_day()
			self.current_day = current_day
	
		#update EVERYTHING
		for entity in self.entities:
			entity.update(now)
				
		self.timestamp = now	
	
	def render(self):
		#render EVERYTHING
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()
		for entity in self.entities:
			entity.render()
		
	def the_lone_range_rides_again(self):
		self.revolve()
		self.render()
