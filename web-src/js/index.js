document.addEventListener("DOMContentLoaded", function(event){
	var previousButton = document.getElementById("previous");
	var playPauseButton = document.getElementById("playpause");
	var nextButton = document.getElementById("next");

	var songInfo = document.getElementById("song-name");
	var artistInfo = document.getElementById("artist-name");
	var albumInfo = document.getElementById("album-name");

	var bubbles = document.querySelectorAll("div.bubble");

	var ws = new WebSocket("ws://" + window.location.hostname + ":5001");

	function updateInfo(data) { 
		songInfo.textContent = data.song;
		artistInfo.textContent = data.artist;
		albumInfo.textContent = data.album;
	}

	function manuallyUpdateSong() {
		var request = new XMLHttpRequest();
		request.open("GET", "/get_song_info");
		request.addEventListener("load", function(event) {
			data = JSON.parse(request.responseText);
			updateInfo(data);
		});
		request.send();
	}
	
	function sendTrackCommand(command) {
		var request = new XMLHttpRequest();
		request.open("POST", "/" + command, true);
		request.addEventListener("load", function(event){
			if (request.status === 200) {
				manuallyUpdateSong();
			}
		});
		request.send();
	}

	//We want to put the song on the page after it loads
	manuallyUpdateSong();

	ws.addEventListener("message", function(event){
		data = JSON.parse(event.data);
		updateInfo(data);
	});

	previousButton.addEventListener("click", function(event) {
		sendTrackCommand("previous");
		previousButton.classList.add("animating");
	});

	playPauseButton.addEventListener("click", function(event) {
		sendTrackCommand("play_pause");
		playPauseButton.classList.add("animating");
	});

	nextButton.addEventListener("click", function(event) {
		sendTrackCommand("next");
		nextButton.classList.add("animating");
	});

	Array.prototype.slice.call(bubbles).forEach(function(bubble) {
		bubble.addEventListener("animationend", function(event){
			console.log("finished");
			bubble.parentNode.classList.remove("animating");
		});
	});
});
