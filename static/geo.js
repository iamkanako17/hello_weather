
function success(pos) {
  var lat = pos.coords.latitude;
  var lng = pos.coords.longitude;

  document.getElementById("location").innerHTML = location;
}

function fail(error) {
  window.alert('位置情報の取得に失敗しました。 エラーコード:' + error.code);
}
navigator.geolocation.getCurrentPosition(success, fail);

