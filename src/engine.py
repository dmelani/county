import firmament
import time

class Engine(object):
	def __init__(self, me_q):
		print 'Engine starting...'
		self.me_q = me_q
		self.firmament = firmament.Firmament()
	def run(self):
		while True:
			#do everything
			time.sleep(1)
		pass
