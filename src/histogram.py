from OpenGL.GL import * 
from OpenGL.GLU import * 
from OpenGL.GLUT import * 
import time
import datetime

class Increment(object):
	def __init__(self, amount, duration):
		self.amount = amount
		self.start = time.time()
		self.end = self.start + duration
		self.curr_val = 0.0
		self.is_complete = False
		
	def update(self, ts):
		if ts > self.end:
			self.curr_val = self.amount
			self.is_complete = True
		else:
			self.curr_val = self.amount * (ts - self.start)/(self.end - self.start)

	def get(self):
		return self.curr_val

class Threshold(object):
	def __init__(self, pos, fade_in = 1.0):
		self.pos = pos
		self.alpha = 0.0
		self.inc = Increment(1.0, fade_in)	
	
	def render(self):
		glPushMatrix()
		glTranslate(0.0, self.pos, 0.0)

		glDisable(GL_POLYGON_OFFSET_FILL)
		glColor(0x00/float(0xff), 0xff/float(0xff), 0xff/float(0xff), self.alpha)
		glutWireCube(1)

		glScale(3.0, 0.0, 3.0)

		glPolygonOffset(1.0, 1.0)
		glEnable(GL_POLYGON_OFFSET_FILL)
		glColor(0x00/float(0xff), 0xff/float(0xff), 0xff/float(0xff), 0.4*self.alpha)
		glutSolidCube(1)

		glDisable(GL_POLYGON_OFFSET_FILL)
		glColor(0x00/float(0xff), 0xff/float(0xff), 0xff/float(0xff), self.alpha)
		glutWireCube(1)

		glPopMatrix()

	def update(self, ts):
		if self.inc.is_complete is False:
			self.inc.update(ts)
			self.alpha = self.inc.get()
		
class Bin(object):
	def __init__(self, width = 1, depth = 1, initial_amount = 0):
		self.amount = initial_amount
		self.width = width
		self.depth = depth
		self.flux = []
		self.inc = 0.0
		self.threshold_interval = 100
		self.thresholds = []
		self.last_threshold = 0

	def render_thresholds(self):
		for t in self.thresholds:
			t.render()
	
	def render(self):
		glPushMatrix()
		glTranslate(0, (self.amount + self.inc) / 2.0, 0)
		glScale(self.width, self.amount + self.inc, self.depth)
		
		glPolygonOffset(1.0, 1.0)
		glEnable(GL_POLYGON_OFFSET_FILL)
		glColor(0x00/float(0xff), 0x50/float(0xff), 0x60/float(0xff))
		glutSolidCube(1)

		glDisable(GL_POLYGON_OFFSET_FILL)
		glColor(0x00/float(0xff), 0xff/float(0xff), 0xff/float(0xff))
		glutWireCube(1)

		glPopMatrix()

		self.render_thresholds()

	def add(self, amount):
		self.amount += amount

	def add_over_time(self, amount, seconds):
		self.flux.append(Increment(amount, seconds))

	def update(self, ts):
		self.inc = 0.0
		for a in self.flux:
			a.update(ts)
			if a.is_complete == True:
				self.amount += a.get()
			else:
				self.inc += a.get()
		self.flux = [a for a in self.flux if a.is_complete is False] 
	
		ct = int((self.inc + self.amount) / self.threshold_interval)
		for p in range(self.last_threshold, ct):
			self.thresholds.append(Threshold((p + 1) * self.threshold_interval, 0.1))

		for t in self.thresholds:
			t.update(ts)

class HistogramRow(object):
	def __init__(self, num_bins = 24):
		self.buckets = [Bin() for x in range(num_bins)]
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

	def add_over_time(self, bucket, amount, seconds):
		self.buckets[bucket].add_over_time(amount, seconds)

	def update(self, ts):
		for b in self.buckets:
			b.update(ts)

class Histogram(object):
	def __init__(self, hours = 24, days = 7):
		self.days = [HistogramRow(hours) for x in range(days)]
		self.last_ts = time.time() 	
		self.width = 50.0
		self.depth = 50.0

	def render(self):
		dc = 0	
		glPushMatrix()
		glScale(self.width, 1.0, self.depth)
		for day in self.days:
			glPushMatrix()
			glTranslate(0, 0, -dc)
			day.render()
			glPopMatrix()
			dc += 1
		glPopMatrix()

	def add(self, amount):
		bucket = datetime.datetime.now().hour
		bucket = bucket
		print 'History adding', amount, 'to', bucket
		#self.days[0].add(bucket, amount)
		self.days[0].add_over_time(bucket, amount, 10.0)

	def advance_day(self):
		self.days.pop()
		self.days.insert(0, HistogramRow(24))
		
	def update(self, ts):
		for d in self.days:
			d.update(ts)
