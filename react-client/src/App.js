import React from "react"

function App() {
  const [state, setState] = React.useState([]);
  React.useEffect(() => {
    const evtSource = new EventSource("http://localhost:5000/alprdsse");
    evtSource.onmessage = (event) => {
      const myEvent = JSON.parse(event.data);
      const alprdData = JSON.parse(event.data)
      const alprdDataUuid = alprdData.uuid;
      const alprdDataResult = alprdData.results[0];
      const alprdDataPlate = alprdData.results[0].plate;
      setState(alprdDataResult);
    };
    evtSource.onopen = (event) => {
      console.log(event);
    };
  }, []);
  return (
    <>
      <div>
        {Object.entries(state).map(([id, { photoURL, email }]) => (
          <div>
            <h3>{id}</h3>
          </div>
        ))}
      </div>

    </>
  );
}

export default App;
