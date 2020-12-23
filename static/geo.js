window.onload = function getPosition() {
    navigator.geolocation.getCurrentPosition(success);
}

function success(pos) {
    var lat = pos.coords.latitude;
    var lon = pos.coords.longitude;
    
    document.getElementById("lat").innerHTML = lat;
    document.getElementById("lon").innerHTML = lon;
}

function reload() {
    
}