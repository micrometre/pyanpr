import { render } from 'https://esm.sh/preact@10.7.2';
import { useState, useCallback } from 'https://esm.sh/preact@10.7.2/hooks';
import { html } from 'https://esm.sh/htm@3.0.4/preact';

const INITIAL_TODOS = [
  { text: 'add HTM imports', done: true },
  { text: 'remove bundler', done: true },
  { text: 'write code', done: false }
];

function App() {
  const [todos, setTodos] = useState(INITIAL_TODOS);
  const [state, setState] = useState([]);

  const evtSource = new EventSource("http://172.187.216.226:5000/alprdsse");
  evtSource.onmessage = (event) => {
    const alprdData = JSON.parse(event.data)
    setState(alprdData)
    console.log(state)
  };

  const add = useCallback(e => {
    const text = e.target.todo.value;
    setTodos(todos => todos.concat({ text, done: false }));
  }, []);
  
  const updateTodo = useCallback(todo => {
    setTodos(todos => todos.slice());
  }, []);

  return html`
    <div class="app">
      ${state}
    </div>
  `;
}

function Todo({ todo, onChange }) {
  const toggle = useCallback(e => {
    todo.done = !todo.done;
    onChange();
  }, []);

  return html`
    <li>
      <label>
        <input type="checkbox" checked=${todo.done} onClick=${toggle} />
        ${todo.text}
      </label>
    </li>
  `;
}

render(html`<${App} />`, document.body);