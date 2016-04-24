import flask
from . import track

app = flask.Flask(__name__)

@app.route("/")
def root():
	return "{} by {} - {}"
