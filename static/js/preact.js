import { render } from 'https://esm.sh/preact@10.7.2';
import { useState } from 'https://esm.sh/preact@10.7.2/hooks';
import { html } from 'https://esm.sh/htm@3.0.4/preact';

function App() {

  return html`
    <div class="app">
      <${Plates}/>
      <${PlatesImages}/>
    </div>
  `;
}
function Plates() {
  const [state, setState] = useState([]);

  const evtSource = new EventSource("http://172.187.216.226:5000/alprdsse");
  evtSource.onmessage = (event) => {
    const alprdData = JSON.parse(event.data)
    setState(alprdData)
  };


  return html`
    <div class="app">
      ${state}
    </div>
  `;

}

function PlatesImages() {
  const [state, setState] = useState([]);

  const evtSource = new EventSource("http://172.187.216.226:5000/images");
  evtSource.onmessage = (event) => {
    const alprdData = JSON.parse(event.data)
    setState(alprdData)
  };


  return html`
    <div class="app">
      <div className="thumbnail">
          <div className="frame">
      ${state}
        <a href=${state} target="_blank" rel="noopener noreferrer">
        <img
            src=${state}
          /> 
        </a>
          </div>
        </div>
    </div>
  `;

}

render(html`<${App} />`, document.body);