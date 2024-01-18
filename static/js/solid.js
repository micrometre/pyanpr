import { onCleanup, createSignal } from "https://esm.sh/solid-js@1.8.1";
import { render } from "https://esm.sh/solid-js@1.8.1/web";
import html from "https://esm.sh/solid-js@1.8.1/html";


const Plates = () => {
  const [plates, setPlates] = createSignal([])
  var source = new EventSource("http://172.187.216.226:5000/alprdsse");
  source.onmessage = function (event) {
    const alprdData = JSON.parse(event.data)
    setPlates(alprdData)
  };
  return html`
    <div>${plates}</div>
    `;
};
render(Plates, document.body);

const PlatesImages = () => {
  const [PlatesImages, setPlatesImages] = createSignal([])

  var source = new EventSource("http://172.187.216.226:5000/images");
  source.onmessage = function (event) {
    const alprdData = JSON.parse(event.data)
    console.log(alprdData)
    setPlatesImages(alprdData)
  };
  return html`
    <div>${PlatesImages}</div>
    <img src=${PlatesImages} alt="Solid logo" />
    `;
};
render(PlatesImages, document.body);
