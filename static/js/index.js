function sendTrackCommand(e){var n=new XMLHttpRequest;n.open("POST","/"+e,!0),n.send()}document.addEventListener("DOMContentLoaded",function(e){var n=document.getElementById("previous"),t=document.getElementById("playpause"),d=document.getElementById("next");n.addEventListener("click",function(e){sendTrackCommand("previous")}),t.addEventListener("click",function(e){sendTrackCommand("play_pause")}),d.addEventListener("click",function(e){sendTrackCommand("next")})});