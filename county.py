import config
import src.receiver as receiver
import Queue
import threading
import sys
import signal

class County(object):
	def __init__(self):
		signal.signal(signal.SIGINT, self.interrupt_handler)
		
		self.rec_q = Queue.Queue()
		self.receiver = receiver.Receiver(('', config.port), self.rec_q)
		self.rec_thread = threading.Thread(target=self.receiver.serve_forever)
		self.rec_thread.daemon = True

		

	def run(self):
		self.rec_thread.start()
		while True:
			self.rec_thread.join(10.0)
	
	def interrupt_handler(self, signum, frame):
		#do cleanup here
		sys.exit(0)

if __name__ == '__main__':
	c = County()
	c.run()

