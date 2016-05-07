function sendTrackCommand(command) {
	var request = new XMLHttpRequest();
	request.open("POST", "/" + command, true);
	request.send();
}

document.addEventListener("DOMContentLoaded", function(event){
	var previousButton = document.getElementById("previous");
	var playPauseButton = document.getElementById("playpause");
	var nextButton = document.getElementById("next");

	var songInfo = document.getElementById("song-name");
	var artistInfo = document.getElementById("artist-name");
	var albumInfo = document.getELementById("album-name");

	function updateInfo(data) { 
		songInfo.textContent = data.song;
		artistInfo.textContent = data.artist;
		albumInfo.textContent = data.album;
	}

	previousButton.addEventListener("click", function(event) {
		sendTrackCommand("previous");
	});

	playPauseButton.addEventListener("click", function(event) {
		sendTrackCommand("play_pause");
	});

	nextButton.addEventListener("click", function(event) {
		sendTrackCommand("next");
	});
});
