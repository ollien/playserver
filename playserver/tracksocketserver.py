import autobahn.asyncio.websocket
import asyncio

class TrackSocket(autobah.asyncio.websocket.WebSocketServerProtocol):
	@asyncio.coroutine
	def onOpen(self):
		#TODO: Make this add to the client list
		print("opened")

	def closed(self, wasClean, code, reason):
		#TODO: make this remove from the client list
		print("closed")

class TrackSocketServerFactory(autobah.asyncio.websocket.WebSocketServerFactory):
	def __init__(self, url):
		super().__init__(self, url)
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
		hostAddr = "ws://{}:{}".format(host, port)
		serverFactory = TrackSocketServerFactory(hostAddr)
		asyncio.set_event_loop(self.loop)
		serverInit = loop.create_server(serverFacotry, host, port)
		server = loop.run_until_complete(serverInit)
		server.run_forever()
