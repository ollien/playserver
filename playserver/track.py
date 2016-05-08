import osascript
from . import configmanager

APP_CONFIG_PATH = "applications/"

controller = TrackController()

class _TrackController():
	
	def __init__(self, application = "radiant")
		self.currentApplication = application
		self._applicationConfigs = configmanager.ConfigManager(APP_CONFIG_PATH)

	def setApplication(self, name):
		self.currentApplication = name

	def getAvailableApplications(self):
		return list(self._applicationConfigs._configs.keys())

	def getCurrentConfig(self):
		return self._applicationConfigs[currentApplication]

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

	def getCurrentArtist():
		result = self._executeCommand("currentartist")
		#Return stdout if there is no error, stderr if otherwise
		if result[0] == 0:
			return result[1]
		else:
			return result[2]
