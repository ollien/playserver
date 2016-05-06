import autobahn.asyncio.websocket


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
