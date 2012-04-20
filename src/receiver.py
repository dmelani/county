import time
import SocketServer

class ReceiverHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		print "received udp packet"
		self.server.queue.put_nowait('derp')	
		print "qsize:", self.server.queue.qsize()
	
class Receiver(SocketServer.UDPServer):
	def __init__(self, server_address, queue):
		self.queue = queue
		SocketServer.UDPServer.__init__(self, server_address, ReceiverHandler)

if __name__ == '__main__':
	import Queue
	queue = Queue.Queue()
	server = Receiver(('localhost', 9999), queue)
	server.serve_forever()
