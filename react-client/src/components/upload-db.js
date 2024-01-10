import React from "react"


const url = "http://172.187.216.226:5000/upload"
export default  function UploadDb() {
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
      <button onClick={() => setIsSending(true)}>Get new user</button>
      <code>{data.plate}</code>
      <code>{data.img}</code>
      <code>{data.confidence}</code>
    </>
  );
}
