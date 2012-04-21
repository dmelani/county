import config
import src.receiver as receiver
import src.mediator as mediator
import src.engine as engine
import multiprocessing
import sys
import signal

class County(object):
	def __init__(self):
		self.rm_q = multiprocessing.Queue()
		self.me_q = multiprocessing.Queue()

		self.receiver = receiver.Receiver(('', config.port), self.rm_q)
		self.rec_proc = multiprocessing.Process(target=self.receiver.run)
		self.rec_proc.daemon = True

		self.mediator = mediator.Mediator(self.rm_q, self.me_q)
		self.med_proc = multiprocessing.Process(target=self.mediator.run)
		self.med_proc.daemon = True

		self.engine = engine.Engine(self.me_q)
		signal.signal(signal.SIGINT, self.interrupt_handler)

	def run(self):
		self.rec_proc.start()
		self.med_proc.start()

		self.engine.run()
	
		self.kill_children()
		sys.exit(0)

	def interrupt_handler(self, signum, frame):
		#do cleanup here
		self.kill_children()
		sys.exit(0)
	
	def kill_children(self):
		print 'And all the children shall die...'
		if self.rec_proc.is_alive():
			print "Killing receiver"
			self.rec_proc.terminate()
			self.rec_proc.join()
		if self.med_proc.is_alive():
			print "Killing mediator"
			self.med_proc.terminate()
			self.med_proc.join()
		print 'done'
	
if __name__ == '__main__':
	c = County()
	c.run()
	print 'Time to quit'

