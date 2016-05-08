import flask
import json
import os.path
import asyncio
import threading
from . import track
from . import tracksocketserver

TEMPLATE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../templates"))
STATIC_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../static"))

#Intialize Flask App
app = flask.Flask(__name__, template_folder = TEMPLATE_PATH, static_folder = STATIC_PATH)

#Start Websocket Thread
loop = asyncio.get_event_loop()
socketServ = tracksocketserver.TrackSocketServer(loop, host = "0.0.0.0")
socketThread = threading.Thread(None, socketServ.run)
socketThread.start()

#Begin Flask routes
@app.route("/")
def root():
	return flask.render_template("index.html")

@app.route("/get_song_info")
def getSongInfo():
	return json.dumps({
		"song": track.controller.getCurrentSong(),
		"artist": track.controller.getCurrentArtist(),
		"album": track.controller.getCurrentAlbum()
	})

@app.route("/get_player_state")
def getPlayerState():
	return json.dumps({
		"playing": track.controller.isPlaying()
	})

@app.route("/play_pause", methods = ["POST"])
def playPause():
	track.controller.playPause()
	return ""

@app.route("/next", methods = ["POST"])
def next():
	track.controller.next()
	return ""

@app.route("/previous", methods = ["POST"])
def previous():
	track.controller.previous()
	return ""

@app.route("/get_applications")
def getApplications():
	return json.dumps(track.controller.getAvailableApplications())

@app.route("/set_application", methods = ["POST"])
def setApplication():
	if "application" in request.form:
		setApplication(request.form["application"])
		return {"error": 0}
	else:
		return {"error": 1}, 400
