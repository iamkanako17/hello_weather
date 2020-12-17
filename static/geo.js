
function success(pos) {
    var lat = pos.coords.latitude;
    var lng = pos.coords.longitude;

    document.getElementById("location").innerHTML = location;
    weatherLink = `http://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lng}&appid=8cac92499bde2ad6dcf5ec1e3a1c9691`;
}

function fail(error) {
  window.alert('位置情報の取得に失敗しました。 エラーコード:' + error.code);
}
navigator.geolocation.getCurrentPosition(success, fail);

