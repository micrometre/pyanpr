import React from "react"
export default function Alprd() {
  const [state, setState] = React.useState([]);
  const [stateUuid, setUud] = React.useState([]);
  React.useEffect(() => {
    const evtSource = new EventSource("http://172.187.216.226:5000/alprdsse");
    evtSource.onmessage = (event) => {
      const alprdData = JSON.parse(event.data)
      const alprdDataUuid = alprdData.uuid;
      const alprdDataResultArray = alprdData.results[0];
      const alprdDataResultArrayMap = Object.keys(alprdDataResultArray).map((key) => [key, alprdDataResultArray[key]]);
      setUud(alprdDataUuid)
      setState(alprdDataResultArrayMap);
    };
    evtSource.onopen = (event) => {
    };
  }, []);
  return (
    <>
                {state[0]}
                <br />
                {stateUuid}
                <br />
                {state[4]}
                <br />
                {state[1]}
                <br />
                {state[7]}
    </>
  );
}