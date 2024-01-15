

    
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
