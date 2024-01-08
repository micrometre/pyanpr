import React from "react";

export default function UploadDb() {
  const [state, setState] = React.useState([]);
  const [ALprDataState, setAlprData] =  React.useState(null);
  React.useEffect(() => {
    fetch("http://172.187.216.226:5000/uploaddb", {
      method: "GET",
      headers: {
        "X-RapidAPI-Key": "your-api-key",
        "X-RapidAPI-Host": "jokes-by-api-ninjas.p.rapidapi.com",
      },
    })
      .then((response) => response.json())
      .then((data) => {
        const uploadArray = Object.keys(data).map((key) => [key, data[key]]);
        console.log((data));
        console.log((uploadArray));
        setState(uploadArray)
        setAlprData(data);
      })
      .catch((error) => console.log(error));
  }, []);
  return (
    <div>
      <h2>Joke of the day:

      </h2>
    </div>
  );
}