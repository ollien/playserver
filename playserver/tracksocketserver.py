import autobahn.asyncio.websocket
import asyncio
import json
from . import track

class TrackSocket(autobahn.asyncio.websocket.WebSocketServerProtocol):

	def onOpen(self):
		self.factory.clients.append(self)

	def onClose(self, wasClean, code, reason):
		self.factory.clients.remove(self)

class TrackSocketServerFactory(autobahn.asyncio.websocket.WebSocketServerFactory):
	def __init__(self, url):
		super().__init__(url)
		self.clients = []
	
	def broadcastMessage(self, message):
		for client in self.clients:
			client.sendMessage(message.encode("utf-8"))

class TrackSocketServer():
	def __init__(self, loop = None, host="127.0.0.1", port=5001):
		self.host = host
		self.port = port

		if loop is None:
			self.loop = asyncio.get_event_loop()	
		else:
			self.loop = loop

		hostAddr = "ws://{}:{}".format(self.host, self.port)
		self.factory = TrackSocketServerFactory(hostAddr)
		
	def run(self):
		asyncio.set_event_loop(self.loop)
		self.factory.protocol = TrackSocket
		track.checker.registerListener(self.transmitTrackChange)
		serverInit = self.loop.create_server(self.factory, self.host, self.port)
		server = self.loop.run_until_complete(serverInit)
		self.loop.run_forever()

	def transmitTrackChange(self, data):
		self.factory.broadcastMessage(json.dumps(data))
