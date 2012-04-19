import config
import src.receiver.Receiver as Receiver
import Queue

class County(object):
	def __init__(self):
		self.rec_q = Queue.Queue()
		self.receiver = Receiver(self.rec_q)
		pass
	def run(self):
		pass

if __name__ == '__main__':
	c = County()
	c.run()
