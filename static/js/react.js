function ReactApp() {
    return (
        <div>React App </div>
    );
}


function ReactAppFromCDN() {
    return (
        <div>

            <ReactApp></ReactApp>
            with CDN

        </div>
    );
}

ReactDOM.render(<ReactAppFromCDN />, document.querySelector('#root'));