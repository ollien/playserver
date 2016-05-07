import autobahn.asyncio.websocket
import asyncio

class TrackSocket(autobahn.asyncio.websocket.WebSocketServerProtocol):

	def onConnect(self, request):
		print("Client connecting: {}".format(request.peer))

	def onOpen(self):
		#TODO: Make this add to the client list
		print("opened")

	def onClose(self, wasClean, code, reason):
		#TODO: make this remove from the client list
		print("closed")

class TrackSocketServerFactory(autobahn.asyncio.websocket.WebSocketServerFactory):
	def __init__(self, url):
		super().__init__(url)
		self.clients = []
	
	def broadcastMessage(self, message):
		for client in selfclients:
			client.sendMessage(message)

class TrackSocketServer():
	def __init__(self, loop = None, host="127.0.0.1", port=5001):
		self.host = host
		self.port = port

		if loop is None:
			self.loop = asyncio.get_event_loop()	
		else:
			self.loop = loop
		
	def run(self):
		hostAddr = "ws://{}:{}".format(self.host, self.port)
		serverFactory = TrackSocketServerFactory(hostAddr)
		serverFactory.protocol = TrackSocket
		asyncio.set_event_loop(self.loop)
		serverInit = self.loop.create_server(serverFactory, self.host, self.port)
		server = self.loop.run_until_complete(serverInit)
		self.loop.run_forever()
