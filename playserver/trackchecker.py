from threading import Timer
from . import track

_listeners = []

class TrackChecker():
	def __init__(self, interval = 5):
		self.listeners = []
		self.CHECK_INTERVAL = interval
		self._generator = self._checkSongGenerator()
		self.timer = None

	def _checkSongGenerator(self):
		while True:
			currentSong = ""
			currentArtist = ""
			currentAlbum = ""
			song = track.getCurrentSong()
			artist = track.getCurrentArtist()
			album = track.getCurrentAlbum()

			if (song != currentSong or artist != currentArtist 
				or album != currentAlbum):
				currentSong = song
				currentArtist = artist
				currentAlbum = album
				self._callListeners()
			yield

	def checkSong(self):
		next(self._generator)
		if self.timer != None:
			self.startTimer()

	def registerListener(self, function):
		_listeners.append(function)

	def _callListeners(self):
		for listener in _listeners:
			listener()

	def startTimer(self):
		self.timer = Timer(self.CHECK_INTERVAL, self.checkSong)
		self.timer.start()

	def cancelTimer(self):
		self.timer.cancel()
