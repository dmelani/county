import time

class Engine(object):
	last_event = None
	last_num_lines = 0

	def __init__(self, re_q, ev_q):
		self.re_q = re_q
		self.ev_q = ev_q

	def run(self):
		while True:
			data = self.re_q.get(True)
			self.handle_event(data)
	
	def handle_event(self, data):
		timestamp, lines = data
		try:
			lines = int(lines)
		except ValueError:
			lines = None

		if lines and self.last_event < timestamp:
			increment = lines - self.last_num_lines
			print 'Engine routing event: add', increment
			self.ev_q.put(('add', increment), True)
			self.last_num_lines = lines
			self.last_event = timestamp
