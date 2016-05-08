import osascript
from . import configmanager

APP_CONFIG_PATH = "applications/"

applicationConfigs = configmanager.ConfigManager(APP_CONFIG_PATH)
#TODO: Make this user choosable
currentApplication = "radiant"

def getCurrentConfig():
	return applicationConfigs[currentApplication]

def _executeCommand(command):
	config = getCurrentConfig()
	fullCommand = "tell application \"{}\" to {}".format(config["name"],
		config["commands"][command])
	return osascript.osascript(fullCommand)

def isPlaying():
	playerStates = getCurrentConfig()["player-states"]
	result = _executeCommand("state")

	if (result[1] == playerStates["stopped"] or
		result[1] == playerStates["paused"]):
		return False
	else:
		return True

def playPause():
	_executeCommand("playpause")

def next():
	_executeCommand("next")

def previous():
	_executeCommand("previous")

def getCurrentSong():
	result = _executeCommand("currentsong")
	#Return stdout if there is no error, stderr if otherwise
	if result[0] == 0:
		return result[1]
	else:
		return result[2]

def getCurrentAlbum():
	result = _executeCommand("currentalbum")
	#Return stdout if there is no error, stderr if otherwise
	if result[0] == 0:
		return result[1]
	else:
		return result[2]

def getCurrentArtist():
	result = _executeCommand("currentartist")
	#Return stdout if there is no error, stderr if otherwise
	if result[0] == 0:
		return result[1]
	else:
		return result[2]
