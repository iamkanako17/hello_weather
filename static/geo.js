
window.onload = function getPosition() {
    navigator.geolocation.getCurrentPosition(success);
    function success(pos) {
        var lat = pos.coords.latitude;
        var lon = pos.coords.longitude;
        
        document.getElementById("lat").value = lat;
        document.getElementById("lon").value = lon;
        document.forms["send"].submit("/weather");
    }
}