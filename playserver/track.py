import osascript
from threading import Timer
from . import configmanager

APP_CONFIG_PATH = "applications/"

class _TrackController():
	
	def __init__(self, application = "radiant"):
		self.currentApplication = application
		self._applicationConfigs = configmanager.ConfigManager(APP_CONFIG_PATH)

	def setApplication(self, name):
		self.currentApplication = name
		checker._callListeners()

	def getAvailableApplications(self):
		configs = self._applicationConfigs._configs
		return [{"name": configs[app]["name"], 
			"key": app, 
			"current": self.currentApplication == app} 
			for app in configs]

	def getCurrentConfig(self):
		return self._applicationConfigs[self.currentApplication]

	def _executeCommand(self, command):
		config = self.getCurrentConfig()
		fullCommand = "tell application \"{}\" to {}".format(config["name"],
			config["commands"][command])
		return osascript.osascript(fullCommand)

	def isPlaying(self):
		playerStates = self.getCurrentConfig()["player-states"]
		result = self._executeCommand("state")

		if (result[1] == playerStates["stopped"] or
			result[1] == playerStates["paused"]):
			return False
		else:
			return True

	def playPause(self):
		self._executeCommand("playpause")

	def next(self):
		self._executeCommand("next")

	def previous(self):
		self._executeCommand("previous")

	def getCurrentSong(self):
		result = self._executeCommand("currentsong")
		#Return stdout if there is no error, stderr if otherwise
		if result[0] == 0:
			return result[1]
		else:
			return result[2]

	def getCurrentAlbum(self):
		result = self._executeCommand("currentalbum")
		#Return stdout if there is no error, stderr if otherwise
		if result[0] == 0:
			return result[1]
		else:
			return result[2]

	def getCurrentArtist(self):
		result = self._executeCommand("currentartist")
		#Return stdout if there is no error, stderr if otherwise
		if result[0] == 0:
			return result[1]
		else:
			return result[2]
	
	def getSystemVolume(self):
		return osascript.osascript("output volume of (get volume settings)")[1]
	
	def setSystemVolume(self, volume):
		osascript.osascript("set volume output volume {}".format(volume))

class _TrackChecker():
	def __init__(self, interval = 5):
		self.listeners = []
		self.CHECK_INTERVAL = interval
		self.currentSong = ""
		self.currentArtist = ""
		self.currentAlbum = ""
		self.playing = False
		self.timer = None

	def checkSong(self):
		song = controller.getCurrentSong()
		artist = controller.getCurrentArtist()
		album = controller.getCurrentAlbum()
		playing = controller.isPlaying()

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
			"song": controller.getCurrentSong(),
			"artist": controller.getCurrentArtist(),
			"album": controller.getCurrentAlbum(),
			"playing": controller.isPlaying()
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

controller = _TrackController()
checker = _TrackChecker(interval = 2)
checker.startTimer()
