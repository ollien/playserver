function sendTrackCommand(command) {
	var request = new XMLHttpRequest();
	request.open("POST", "/" + command, true);
	request.send();
}

document.addEventListener("DOMContentLoaded", function(event){
	var previousButton = document.getElementById("previous");
	var playPauseButton = document.getElementById("playpause");
	var nextButton = document.getElementById("next");

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
