import config
import src.receiver as receiver
import src.engine as engine
import multiprocessing
import sys
import signal

class County(object):
	def __init__(self):
		signal.signal(signal.SIGINT, self.interrupt_handler)
		
		self.re_q = multiprocessing.Queue()
		self.ev_q = multiprocessing.Queue()

		self.receiver = receiver.Receiver(('', config.port), self.re_q)
		self.rec_proc = multiprocessing.Process(target=self.receiver.serve_forever)
		self.rec_proc.daemon = True

		self.engine = engine.Engine(self.re_q, self.ev_q)
		self.eng_proc = multiprocessing.Process(target=self.engine.run)
		self.eng_proc.daemon = True

	def run(self):
		self.rec_proc.start()
		self.eng_proc.start()
		while True:
			self.rec_proc.join(10.0)
			self.eng_proc.join(10.0)
	
	def interrupt_handler(self, signum, frame):
		#do cleanup here
		sys.exit(0)

if __name__ == '__main__':
	c = County()
	c.run()

