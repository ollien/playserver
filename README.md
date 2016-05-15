PlayServer
===========

Have you ever wanted to control your music from another device in your home? Look no further than PlayServer! Built on Flask, websockets, and osascript, PlayServer will allow you to control your music from any device.

Requirements
------------
Currently, PlayServer only works on Mac OSX due to its extensive use of osascript. **Make sure you have osascript installed!**

Supported Applications
----------------------
Out of the box, PlayServer only supports iTunes, Spotify, and Radiant Player. However, you can add whatever application you want. Simply create a new JSON file in the applications directory, and add the appropriate osascript commands for your application. For instance, this is the iTunes config file.

```json
{
	"name": "iTunes",
	"commands": {
		"playpause": "playpause",
		"next": "next track",
		"previous": "previous track",
		"currentsong": "get name of current track",
		"currentalbum": "get album of current track",
		"currentartist": "get artist of current track",
		"state": "get player state"
	},
	"player-states": {
		"stopped": "stopped",
		"paused": "paused",
		"playing": "playing"
	}
}
```

The "name" attribute is the application that will be controlled via osascript. The "commands" object holds all commands supported by PlayServer. For instance, when PlayServer looks to skip to the next song, it will run `tell application "iTunes" to next track`. "iTunes" was extracted from the "name" attribute and "next track" was extracted from commands.next. Because some applications use different verbs for their player states, a "player-states" object is provided. For instance, if an application's "stopped" state is 0, then player-states.stopped should be equal to "0."

Usage
-----
PlayServer can be run standalone by simply running the `run` script provided. Alternatively, it can be run using a wsgi middleware server such as uwsgi. The wsgi file is located in playserver/wsgi.py

License
-------
MIT
