import autobahn.asyncio.websocket


class TrackSocket(autobah.asyncio.websocket.WebSocketServerProtocol):
	@asyncio.coroutine
	def onOpen(self):
		#TODO: Make this add to the client list
		print("opened")

	def closed(self, wasClean, code, reason):
		#TODO: make this remove from the client list
		print("closed")
