







if (typeof (EventSource) !== "undefined") {
  var source = new EventSource("http://172.187.216.226:5000/alprdsse");
  source.onmessage = function (event) {

    const reducer = (state = []) => {
      return state;
    };
    const store = Redux.createStore(reducer);

    store.subscribe(() => {
      console.log('subscribe', store.getState());
    });


    store.dispatch({ type: "ADD_USER" });

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
    alpr.innerHTML += event.data.replace(/[{("")}]/g, '') + "<br>";
    alprImg.src = event.data.replace(/[{("")}]/g, '');
    box.insertBefore(alpr, box.firstChild)
    box.insertBefore(alprImg, box.firstChild)
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