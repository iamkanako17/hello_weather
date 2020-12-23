function getPosition() {
    navigator.geolocation.getCurrentPosition(success);
}

function success(position) {
    var lat = position.coords.latitude;
    var lon = position.coords.longitude;
    
    document.getElementById("lat").innerHTML = lat;
    document.getElementById("lon").innerHTML = lon;
}