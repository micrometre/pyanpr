import React from "react";

export default function UploadDb() {
  const [state, setState] = React.useState([]);
  const [ALprDataState, setAlprData] =  React.useState(null);
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
    <div>
      <h2>
        {state.confidence}
        {state.plate}
        {state.img}
      </h2>
    </div>
  );
}