import config
import src.receiver as receiver
import src.mediator as mediator
import multiprocessing
import sys
import signal

class County(object):
	def __init__(self):
		signal.signal(signal.SIGINT, self.interrupt_handler)
		
		self.rm_q = multiprocessing.Queue()
		self.me_q = multiprocessing.Queue()

		self.receiver = receiver.Receiver(('', config.port), self.rm_q)
		self.rec_proc = multiprocessing.Process(target=self.receiver.serve_forever)
		self.rec_proc.daemon = True

		self.mediator = mediator.Mediator(self.rm_q, self.me_q)
		self.med_proc = multiprocessing.Process(target=self.mediator.run)
		self.med_proc.daemon = True

	def run(self):
		self.rec_proc.start()
		self.med_proc.start()
		while True:
			self.rec_proc.join(10.0)
			self.med_proc.join(10.0)
	
	def interrupt_handler(self, signum, frame):
		#do cleanup here
		sys.exit(0)

if __name__ == '__main__':
	c = County()
	c.run()

