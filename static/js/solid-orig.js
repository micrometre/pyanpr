import { onCleanup, createSignal, createResource } from "https://esm.sh/solid-js@1.8.1";
import { render } from "https://esm.sh/solid-js@1.8.1/web";
import html from "https://esm.sh/solid-js@1.8.1/html";
const Search = () => {
    const [plates, setPlates] = createSignal([])
    let file2 = `http://127.0.0.1:5000/check_key?key=alpr_plate_to_id&field=AJ13SYV`
    let text = document.getElementById("field").value;
    function getText() {
        console.log(text)
    }


    return html`
     <div class="position-relative overflow-hidden p-1 p-md-1 m-md-1 text-center">
        <form action="/check_key" method="get">
            <label for="key">key:</label>
            <input type="text" id="key" name="key"><br><br>
            <label for="field">field:</label>
            <input type="text" id="field" name="field"><br><br>
            <input type="submit" value="Submit"><br><br>
            <input id="field" name="field" type="text" oninput=${getText}  placeholder="Enter ALPR">
          </form> 
    </div>
    `;
};
render(Search, document.body);

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
render(Plates, document.body);

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
        <div  id="alpr-image-div" >${PlatesImages}</div>
    </div>




    `;
};
render(PlatesImages, document.body);