import flask
from . import track

app = flask.Flask(__name__)

@app.route("/")
def root():
	song = track.getCurrentSong()
	artist = track.getCurrentArtist()
	album = track.getCurrentAlbum()
	return "{} by {} - {}".format(song, artist, album)
