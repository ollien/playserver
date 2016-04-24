import flask
from . import track

app = flask.flask(__name__)

@app.route("/")
def root():
	return "{} by {} - {}"
