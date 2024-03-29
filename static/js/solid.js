import { onCleanup, createSignal, createResource } from "https://esm.sh/solid-js@1.8.1";
import { render } from "https://esm.sh/solid-js@1.8.1/web";
import html from "https://esm.sh/solid-js@1.8.1/html";

const cameraPlates = () => {
    const [plates, setPlates] = createSignal([])
    var source = new EventSource("http://127.0.0.1:5000/camerasse");
    source.onmessage = function (event) {
        const alprdData = JSON.parse(event.data)
        setPlates(alprdData)
    };
    return html`
     <div class="position-relative overflow-hidden p-1 p-md-1 m-md-1 text-center">
        <h2 class="pt-2 mt-2 mb-2 display-4 fw-bold">
        ${plates}
       </h2>
    </div>
    `;
};
render(cameraPlates, document.getElementById('alprd-plates-camera'));



const PlatesImages = () => {
    const [PlatesImages, setPlatesImages] = createSignal([])
    function onError(e) {
        e.target.src =
            "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/No_sign.svg/192px-No_sign.svg.png";
    }

    var source = new EventSource("http://127.0.0.1:5000/images");
    source.onmessage = function (event) {
        const alprdData = JSON.parse(event.data)
        setPlatesImages(alprdData)
        const img = document.getElementById("alpr-image")
        img.addEventListener("error", function (event) {
            event.target.src = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/No_sign.svg/192px-No_sign.svg.png";

            event.onerror = null
        })
    };
    return html`


    <div class="position-relative overflow-hidden p-3 p-md-5 m-md-3 text-center">
         <img src=${PlatesImages} class="img-thumbnail" id="alpr-image" alt="...">
        <a target="_blank" href=${PlatesImages}>
        <div  id="alpr-image-div" >${PlatesImages}</div>
        </a>
    </div>

    `;
};
render(PlatesImages, document.getElementById('alprd-images'));



const Plates = () => {
    const [plates, setPlates] = createSignal([])
    var source = new EventSource("http://127.0.0.1:5000/alprdsse");
    source.onmessage = function (event) {
        const alprdData = JSON.parse(event.data)
        setPlates(alprdData)
    };
    return html`
     <div class="position-relative overflow-hidden p-1 p-md-1 m-md-1 text-center">
        <h2 class="pt-2 mt-2 mb-2 display-4 fw-bold">
        ${plates}
       </h2>
    </div>
    `;
};
//render(Plates, document.body);
render(Plates, document.getElementById('alprd-plates'));

