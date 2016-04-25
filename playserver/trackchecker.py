from threading import Timer
from . import track

listeners = []
CHECK_INTERVAL = 5

def _checkSongGenerator():
	while True:
		currentSong = ""
		currentArtist = ""
		currentAlbum = ""
		if (song != currentSong or artist != currentArtist 
			or album != currentAlbum):
			currentSong = song
			currentArtist = artist
			currentAlbum = album
		_callListeners()
		yield

def checkSong():
	next(_generator)

def registerListener(function):
	listeners.append(function)

def _callListeners():
	for listener in listeners:
		listener()

#Must be after function declaration in order to work
_generator = _checkSongGenerator()
timer = Timer(CHECK_INTERVAL, checkSong)
