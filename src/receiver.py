import time
import SocketServer

class ReceiverHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		try:
			(timestamp, data) = self.request[0].split()
			print 'Received packet:', timestamp, data
			self.server.queue.put_nowait((timestamp, data))	
		except Exception:
			print 'MALFORMED DATA RECEIVED'
	
class Receiver(SocketServer.UDPServer):
	def __init__(self, server_address, queue):
		self.queue = queue
		SocketServer.UDPServer.__init__(self, server_address, ReceiverHandler)

if __name__ == '__main__':
	import Queue
	queue = Queue.Queue()
	server = Receiver(('localhost', 9999), queue)
	server.serve_forever()
