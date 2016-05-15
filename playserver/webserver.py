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


@app.before_first_request
def startSocketServer():
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
	reqData = json.loads(flask.request.data.decode("utf-8"))
	if "application" in reqData:
		track.controller.setApplication(reqData["application"])
		return json.dumps({"error": 0})
	else:
		return json.dumps({"error": 1}), 400

@app.route("/get_application")
def getApplication():
	return track.controller.currentApplication	

@app.route("/get_system_volume")
def getSystemVolume():
	return track.controller.getSystemVolume()

@app.route("/set_system_volume")
def setSystemVolume():
	reqData = flask.request.data
	if reqData.isDigit() and 0 < int(reqData) < 100:
		track.controller.setSystemVolume(reqData)
		return json.dumps({"error": 0})
	else:
		return json.dumps({"error": 1}), 400
