document.addEventListener("DOMContentLoaded",function(e){function t(e){l.textContent=e.song,u.textContent=e.artist+" - "+e.album}function n(){var e=new XMLHttpRequest;e.open("GET","/get_song_info"),e.addEventListener("load",function(n){data=JSON.parse(e.responseText),t(data)}),e.send()}function a(e){var t=new XMLHttpRequest;t.open("POST","/"+e,!0),t.addEventListener("load",function(e){200===t.status&&n()}),t.send()}function s(){p?(o.classList.remove("fa-play"),o.classList.add("fa-pause")):(o.classList.remove("fa-pause"),o.classList.add("fa-play"))}function d(){var e=new XMLHttpRequest;e.open("GET","/get_player_state"),e.addEventListener("load",function(t){data=JSON.parse(e.responseText),p=data.playing,s()}),e.send()}var i=document.getElementById("previous"),o=document.getElementById("playpause"),c=document.getElementById("next"),l=document.getElementById("track-line-1"),u=document.getElementById("track-line-2"),r=document.querySelectorAll("div.bubble"),p=!1,m=new WebSocket("ws://"+window.location.hostname+":5001");n(),d(),m.addEventListener("message",function(e){data=JSON.parse(e.data),p=data.playing,t(data),s()}),i.addEventListener("click",function(e){a("previous"),i.classList.add("animating")}),o.addEventListener("click",function(e){a("play_pause"),o.classList.add("animating"),d()}),c.addEventListener("click",function(e){a("next"),c.classList.add("animating")}),Array.prototype.slice.call(r).forEach(function(e){e.addEventListener("animationend",function(t){console.log("finished"),e.parentNode.classList.remove("animating")})})});