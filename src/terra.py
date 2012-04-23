from OpenGL.GL import * 
from OpenGL.GLU import * 
from OpenGL.GLUT import * 
import time
import histogram

class Terra(object):
	def __init__(self):
		self.timestamp = time.time()
		self.entities = []
		self.histogram = histogram.Histogram()
		self.entities.append(self.histogram)

	def add(self, amount):
		self.histogram.add(amount)
	
	def revolve(self):
		now = time.time()
		delta = now - self.timestamp
	
		#update EVERYTHING
		
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
