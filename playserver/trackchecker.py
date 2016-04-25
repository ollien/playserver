from threading import Timer
import track


class TrackChecker():

	currentSong = ""
	currentArtist = ""
	currentAlbum = ""
	timer = Timer(interval, checkSong)
	listeners = []

	@staticmethod
	def checkSong():
		song = track.getCurrentSong()
		artist = track.getCurrentArtist()
		album = track.getCurrentAlbum()
		if (song != currentSong or artist != currentArtist 
			or album != currentAlbum):
			currentSong = song
			currentArtist = artist
			currentAlbum = album
		_callListeners()

	@staticmethod
	def registerListener(func):
		listeners.append(func)	

	@staticmethod
	def _callListeners():
		for listener in listeners:
			listener(currentSong, currentArtist, currentAlbum)
