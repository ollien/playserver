import flask
import json
import os.path
from . import track

TEMPLATE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../templates"))
STATIC_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../static"))

app = flask.Flask(__name__, template_folder = TEMPLATE_PATH, static_folder = STATIC_PATH)

@app.route("/")
def root():
	song = track.getCurrentSong()
	artist = track.getCurrentArtist()
	album = track.getCurrentAlbum()
	return flask.render_template("index.html")

@app.route("/get_song_info")
def getSongInfo():
	return json.dumps({
		"name": track.getCurrentSong(),
		"artist": track.getCurrentAritst(),
		"album": track.getCrrentAlbum()
	})

@app.route("/play_pause", methods = ["POST"])
def playPause():
	track.playPause()
	return ""

@app.route("/next", methods = ["POST"])
def next():
	track.next()
	return ""

@app.route("/previous", methods = ["POST"])
def previous():
	track.previous()
	return ""
