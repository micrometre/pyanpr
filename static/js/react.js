const { useState } = React

const UploadDb = (props) => { 
    const [text, setText] = useState('hello');

    return (
      <div>
        <h1>{text}</h1>
        <input type="text" value={text} onChange={(e) => setText(e.target.value)} />
      </div>
    );
  }


function ReactApp() {
    return (
        <div>React App </div>
    );
}




function ReactAppFromCDN() {
    return (
        <div>

            <UploadDb></UploadDb>
            <ReactApp></ReactApp>
            with CDN

        </div>
    );
}

ReactDOM.render(<ReactAppFromCDN />, document.querySelector('#root'));