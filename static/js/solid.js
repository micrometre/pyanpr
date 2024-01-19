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
    function onError(e) {
        e.target.src =
            "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/No_sign.svg/192px-No_sign.svg.png";
    }

    var source = new EventSource("http://172.187.216.226:5000/images");
    source.onmessage = function (event) {
        const alprdData = JSON.parse(event.data)
        console.log(alprdData)
        setPlatesImages(alprdData)
        const img = document.getElementById("alpr-image")
        img.addEventListener("error", function (event) {
            event.target.src = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/No_sign.svg/192px-No_sign.svg.png";

            event.onerror = null
        })
    };
    return html`
            <img src=${PlatesImages} class="img-thumbnail" id="alpr-image" alt="...">
    <div  id="alpr-image-div" >${PlatesImages}</div>
    `;
};
render(PlatesImages, document.body);