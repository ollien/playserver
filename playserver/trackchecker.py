from threading import Timer
from . import track

_listeners = []

class TrackChecker():
	def __init__(self, interval = 5):
		self.listeners = []
		self.CHECK_INTERVAL = interval
		self.currentSong = ""
		self.currentArtist = ""
		self.currentAlbum = ""
		self.timer = None

	def checkSong(self):
		song = track.getCurrentSong()
		artist = track.getCurrentArtist()
		album = track.getCurrentAlbum()

		if (song != self.currentSong or artist != self.currentArtist 
			or album != self.currentAlbum):
			self.currentSong = song
			self.currentArtist = artist
			self.currentAlbum = album
			self._callListeners()
		
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
		self.timer = None
