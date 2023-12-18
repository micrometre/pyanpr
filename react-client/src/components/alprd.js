import React from "react"
export default function Alprd() {
  const [state, setState] = React.useState([]);
  const [stateUuid, setUud] = React.useState([]);
  React.useEffect(() => {
    const evtSource = new EventSource("http://localhost:5000/alprdsse");
    evtSource.onmessage = (event) => {
      const alprdData = JSON.parse(event.data)
      const alprdDataUuid = alprdData.uuid;
      const alprdDataResultArray = alprdData.results[0];
      const alprdDataResultArrayMap = Object.keys(alprdDataResultArray).map((key) => [key, alprdDataResultArray[key]]);
      setUud(alprdDataUuid)
      console.log(alprdDataUuid)
      setState(alprdDataResultArrayMap);
    };
    evtSource.onopen = (event) => {
      console.log(event);
    };
  }, []);
  return (
    <>
      <h1 className="text-3xl font-bold underline">
        {stateUuid}
    <br/>
        {state[4]}
    <br/>
        {state[1]}
    <br/>
        {state[7]}
      </h1>
    </>
  );
}