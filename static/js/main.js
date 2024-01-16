


if (typeof (EventSource) !== "undefined") {
  var source = new EventSource("http://172.187.216.226:5000/alprdsse");
  source.onmessage = function (event) {


    const box = document.getElementById('box')
    const alpr = document.createElement('h2')
    alpr.innerHTML += event.data.replace(/[{("")}]/g, '') + "<br>";
    box.insertBefore(alpr, box.firstChild)
  };
} else {
  document.getElementById("result").innerHTML = "Sorry, your browser does not support server-sent events...";
}





















if (typeof (EventSource) !== "undefined") {
  var source = new EventSource("http://172.187.216.226:5000/images");
  source.onmessage = function (event) {
    const box = document.getElementById('image-box')
    const alpr = document.createElement('h2')
    const alprImg = document.createElement('img');
    alprImg.setAttribute('id', 'alpr-image');
    alpr.innerHTML += event.data.replace(/[{("")}]/g, '') + "<br>";
    alprImg.src = event.data.replace(/[{("")}]/g, '');
    box.insertBefore(alpr, box.firstChild)
    box.insertBefore(alprImg, box.firstChild)
    const img = document.getElementById("alpr-image")
    img.addEventListener("error", function (event) {
      event.target.src = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/No_sign.svg/192px-No_sign.svg.png";

      event.onerror = null
    })

  };
} else {
  document.getElementById("result").innerHTML = "Sorry, your browser does not support server-sent events...";
}



function handleFileSelect(evt) {
  for (const file of evt.target.files) {
    const div = document.createElement('div')
    const src = URL.createObjectURL(file)
    div.innerHTML =
      `<img style="height: 250px; border: 1px solid #000; margin: 5px"` +
      `src="${src}" title="${escape(file.name)}">`

    document.getElementById('list').insertBefore(div, null)
  }
}

document.getElementById('files').addEventListener('change', handleFileSelect, false);