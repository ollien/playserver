import configmanager
import osascript

APP_CONFIG_PATH = "../applications/"

applicationConfigs = configmanager.ConfigManager(APP_CONFIG_PATH)
#TODO: Make this user choosable
currentApplication = "radiant"

def getCurrentConfig():
	return applicationConfigs[currentApplication]

def _executeCommand(command):
	config = getCurrentConfig()
	fullCommand = "tell application \"{}\" to {}".format(config["name"],
		config["commands"][command])
	result = osascript.osascript(fullCommand)
	#Return the return code of the command - 0 if succuessful.
	return result[0]
