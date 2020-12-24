const status = document.querySelector('#status');

function success(pos) {
    var lat = pos.coords.latitude;
    var lon = pos.coords.longitude;
    
    document.getElementById("lat").value = lat;
    document.getElementById("lon").value = lon;
    document.forms["send"].submit();
}


function error() {
    status.textContent = '位置情報を取得できません。設定をお確かめください。';
}

if(!navigator.geolocation) {
    status.textContent = 'ご使用のブラウザでは位置情報の取得ができません。';
} else {
    status.textContent = 'Getting your position…';
    navigator.geolocation.getCurrentPosition(success, error);
}