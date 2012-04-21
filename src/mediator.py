import time
import Queue

class Mediator(object):
	last_event = None
	last_num_lines = 0

	def __init__(self, rm_q, me_q):
		print 'Mediator initializing...'
		self.rm_q = rm_q
		self.me_q = me_q

	def start(self):
		while True:
			try:
				data = self.rm_q.get(True, 1.0)
			except Queue.Empty:
				pass
			else:
				self.handle_event(data)
	def run(self):
		try:
			self.start()
		except:
			return
	
	def handle_event(self, data):
		timestamp, lines = data
		try:
			lines = int(lines)
		except ValueError:
			lines = None

		if lines and self.last_event < timestamp:
			increment = lines - self.last_num_lines
			print 'Mediator routing event: add', increment
			self.me_q.put(('add', increment), True)
			self.last_num_lines = lines
			self.last_event = timestamp
