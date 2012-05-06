import time
import SocketServer

class ReceiverHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		try:
			words = self.request[0].split()
			(command, params) = (words[0], words[1:])
			print 'Received packet:', command, params
			self.server.queue.put_nowait((command, params))	
		except Exception:
			print 'MALFORMED DATA RECEIVED'
		except Full:
			pass
	
class Receiver(SocketServer.UDPServer):
	def __init__(self, server_address, queue):
		print 'Receiver powering up...'
		self.queue = queue
		SocketServer.UDPServer.__init__(self, server_address, ReceiverHandler)
	def run(self):
		try:
			self.serve_forever()
		except: 
			return

if __name__ == '__main__':
	import Queue
	queue = Queue.Queue()
	server = Receiver(('localhost', 9999), queue)
	server.serve_forever()
