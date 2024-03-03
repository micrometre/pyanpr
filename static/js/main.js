
function switchStatus() {
    let switchButton = document.getElementById('ledonof');
    let img = document.getElementById('ledPic');
    if (switchButton.value == "Camera-2") {
        img.src = "http://127.0.0.1:5000/video_feed";
        switchButton.value = "camera-1";
    } else {
        img.src = "http://192.168.1.120:8080/video";
        switchButton.value = "Camera-2";
    }
}
let file = "http://127.0.0.1:5000/uploaddb"
fetch(file)
    .then(x => x.text())
    .then(y => document.getElementById("uploaddb").innerHTML = y);

fetch(file)
    .then((response) => {
    });