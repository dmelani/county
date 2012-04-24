from OpenGL.GL import * 
from OpenGL.GLU import * 
from OpenGL.GLUT import * 
import time
import datetime

class Staple(object):
	def __init__(self, width = 1, depth = 1, initial_amount = 0):
		self.amount = initial_amount
		self.width = width
		self.depth = depth

	def render(self):
		glPushMatrix()
		glTranslate(0, self.amount / 2.0, 0)
		glScale(self.width, self.amount, self.depth)
		
		glPolygonOffset(1.0, 1.0)
		glEnable(GL_POLYGON_OFFSET_FILL)
		glColor(0x23/float(0xff), 0x8c/float(0xff), 0x47/float(0xff))
		glutSolidCube(1)

		glDisable(GL_POLYGON_OFFSET_FILL)
		glColor(0x1a/float(0xff), 0xa6/float(0xff), 0x00/float(0xff))
		glutWireCube(1)
		
		glPopMatrix()

	def add(self, amount):
		self.amount += amount

	def update(self, ts):
		pass

class HistogramRow(object):
	def __init__(self, num_staples = 24):
		self.buckets = [Staple() for x in range(num_staples)]
	def render(self):
		bc = 0
		for bucket in self.buckets:
			glPushMatrix()
			glTranslate(bc, 0, 0) 
			bucket.render()
			glPopMatrix()
			bc += 1

	def add(self, bucket, amount):
		self.buckets[bucket].add(amount)

	def update(self, ts):
		for b in self.buckets:
			b.update(ts)

class Histogram(object):
	def __init__(self, hours = 24, days = 7):
		self.days = [HistogramRow(hours) for x in range(days)]
 	
	def render(self):
		dc = 0	
		for day in self.days:
			glPushMatrix()
			glTranslate(0, 0, -dc)
			day.render()
			glPopMatrix()
			dc += 1

	def add(self, amount):
		bucket = datetime.datetime.now().hour
		bucket = bucket
		print 'History adding', amount, 'to', bucket
		self.days[0].add(bucket, amount)

	def advance_day(self):
		self.days.pop()
		self.days.insert(0, HistogramRow(24))
		
	def update(self, ts):
		for d in self.days:
			d.update(ts)
