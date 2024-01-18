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