import React from "react"


const url = "http://172.187.216.226:5000/uploaddb"
export default function UploadDb() {
  const [isSending, setIsSending] = React.useState(false);
  const [data, setData] = React.useState([]);
  console.log(data);

  React.useEffect(() => {
    isSending &&
      fetch(url)
        .then((response) => response.json())
        .then((data) => setData(data))
        .then(() => setIsSending(false));
  }, [isSending]);

  return (
    <>

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
          <h2 
          className={`mb-3 text-2xl font-semibold`}
          >
            confidence
            {' '}
            <span className="inline-block transition-transform group-hover:translate-x-1 motion-reduce:transform-none">
              -&gt;
              <code>{data.confidence}</code>
            </span>
          </h2>
        </div>
    </>
  );
}
