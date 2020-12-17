if( navigator.geolocation ) {
    alert("現在地取得成功");
    navigator.geolocation.getCurrentPosition((position) => {
      doSomething(position.coords.latitude, position.coords.longitude);
    });
} else {
    alert("現在地取得未対応");
}
