document.addEventListener("DOMContentLoaded", function(event){
	var previousButton = document.getElementById("previous");
	var playPauseButton = document.getElementById("playpause");
	var nextButton = document.getElementById("next");

	var line1 = document.getElementById("track-line-1");
	var line2 = document.getElementById("track-line-2");

	var bubbles = document.querySelectorAll("div.bubble");

	var playing = false;
	var ws = new WebSocket("ws://" + window.location.hostname + ":5001");


	function updateInfo(data) { 
		line1.textContent = data.song;
		line2.textContent = data.artist + " - " + data.album;
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

	function togglePlayPauseButton() {
		if (playing) {
			playPauseButton.classList.remove("fa-play");
			playPauseButton.classList.add("fa-pause");
		}
		else {
			playPauseButton.classList.remove("fa-pause");
			playPauseButton.classList.add("fa-play");
		}

	}

	function updatePlayerState() {
		var request = new XMLHttpRequest();
		request.open("GET", "/get_player_state");
		request.addEventListener("load", function(event) {
			data = JSON.parse(request.responseText);
			playing = data.playing;
			togglePlayPauseButton();
		});
		request.send();
	}

	//We want to put the song on the page after it loads
	manuallyUpdateSong();
	updatePlayerState();

	ws.addEventListener("message", function(event){
		data = JSON.parse(event.data);
		playing = data.playing;
		updateInfo(data);
		togglePlayPauseButton();
	});

	previousButton.addEventListener("click", function(event) {
		sendTrackCommand("previous");
		previousButton.classList.add("animating");
	});

	playPauseButton.addEventListener("click", function(event) {
		sendTrackCommand("play_pause");
		playPauseButton.classList.add("animating");
		updatePlayerState();
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
