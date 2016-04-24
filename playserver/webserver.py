import flask
import json
from . import track

app = flask.Flask(__name__)

@app.route("/")
def root():
	song = track.getCurrentSong()
	artist = track.getCurrentArtist()
	album = track.getCurrentAlbum()
	return "{} by {} - {}".format(song, artist, album)

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
