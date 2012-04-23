from OpenGL.GL import * 
from OpenGL.GLU import * 
from OpenGL.GLUT import * 
import time

class Staple(object):
	def __init__(self, width = 1, depth = 1, initial_amount = 0):
		self.amount = initial_amount
		self.width = width
		self.depth = depth

	def render(self):
		glPushMatrix()
		glScale(self.width, self.amount, self.depth)
		glutSolidCube(1)
		glPopMatrix()

	def add(self, amount):
		self.amount += amount

class Histogram(object):
	def __init__(self, num_buckets = 8):
		self.buckets = [Staple()] * num_buckets
 	
	def render(self):	
		for stapel in self.buckets:
			stapel.render()

	def add(self, amount):
		bucket = 0 # XXX Fixme
		print 'History adding', amount, 'to', bucket
		self.buckets[bucket].add(amount)
