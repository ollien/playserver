from threading import Timer
from . import track


class TrackChecker():
	def __init__(self, interval = 5):
		self.listeners = []
		self.CHECK_INTERVAL = interval
		self.currentSong = ""
		self.currentArtist = ""
		self.currentAlbum = ""
		self.playing = False
		self.timer = None

	def checkSong(self):
		song = track.getCurrentSong()
		artist = track.getCurrentArtist()
		album = track.getCurrentAlbum()
		playing = track.isPlaying()

		if (song != self.currentSong or artist != self.currentArtist 
			or album != self.currentAlbum or playing != self.playing):
			self.currentSong = song
			self.currentArtist = artist
			self.currentAlbum = album
			self.playing = playing
			self._callListeners()
		
		if self.timer != None:
			self.startTimer()

	def registerListener(self, function):
		self.listeners.append(function)

	def _callListeners(self):
		data = {
			"song": track.getCurrentSong(),
			"artist": track.getCurrentArtist(),
			"album": track.getCurrentAlbum(),
			"playing": track.isPlaying()
		}

		for listener in self.listeners:
			listener(data)

	def startTimer(self):
		self.timer = Timer(self.CHECK_INTERVAL, self.checkSong)
		self.timer.daemon = True
		self.timer.start()

	def cancelTimer(self):
		self.timer.cancel()
		self.timer = None
