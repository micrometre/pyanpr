import React from "react";

export default function UploadDb() {
  const [state, setState] = React.useState([]);
  const [ALprDataState, setAlprData] = React.useState(null);
  React.useEffect(() => {
    fetch("http://172.187.216.226:5000/upload", {
      method: "GET",
      headers: {
        "X-RapidAPI-Key": "your-api-key",
        "X-RapidAPI-Host": "jokes-by-api-ninjas.p.rapidapi.com",
      },
    })
      .then((response) => response.json())
      .then((data) => {
        console.log((data));
        setState(data)
      })
      .catch((error) => console.log(error));
  }, []);
  return (

    <>
      <div>
        <h2>
          {state.confidence}
          {state.plate}
          {state.img}
        </h2>
      </div>


      <div
        className="group rounded-lg border border-transparent px-5 py-4 transition-colors hover:border-gray-300 hover:bg-gray-100 hover:dark:border-neutral-700 hover:dark:bg-neutral-800/30"
      >
        <h2
          className={`mb-3 text-2xl font-semibold`}
        >
          <button onClick={() => setIsSending(true)}>Get ALPR Data</button>
        </h2>
        <br />
        <h2 className={`mb-3 text-2xl font-semibold`}>
          Licence plate number
          {' '}
          <span className="inline-block transition-transform group-hover:translate-x-1 motion-reduce:transform-none">
            -&gt;
            <code>{data}</code>
          </span>
        </h2>
      </div>
    </>
  );
}