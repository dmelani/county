import time

class Mediator(object):
	last_event = None
	last_num_lines = 0

	def __init__(self, rm_q, me_q):
		self.rm_q = rm_q
		self.me_q = me_q

	def run(self):
		while True:
			data = self.rm_q.get(True)
			self.handle_event(data)
	
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
