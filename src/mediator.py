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
		command = data[0]
		if command == 'add':
			params = data[1]
			timestamp, lines = params
			try:
				timestamp = int(timestamp)
				lines = int(lines)
			except ValueError:
				lines = None

			if lines and self.last_event < timestamp:
				increment = lines - self.last_num_lines
				print 'Mediator routing event: add', increment
				self.me_q.put(('add', increment), True)
				self.last_num_lines = lines
				self.last_event = timestamp

		if command == 'randomize':
			print 'Mediator routing event: randomize'
			self.me_q.put(('randomize', None), True)
		
		if command == 'move_to' or command == 'look_at':
			try:
				x, y, z = data[1]
				x = float(x)
				y = float(y)
				z = float(z)
			except:	
				print 'Mediator received invalid command:', command, parameters
				return	
			else: 
				print 'Mediator routing event: move_to', x, y, z
				self.me_q.put((command, x, y, z), True)
