import time

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
