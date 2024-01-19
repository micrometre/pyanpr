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



function update() {
  var element = document.getElementById("videoprogressBar");
  var width = 1;
  var identity = setInterval(scene, 10);
  function scene() {
    if (width >= 100) {
      clearInterval(identity);
    } else {
      width++;
      element.style.width = width + '%';
    }
  }
}