import React from "react";


export default function Joke() {
  const [joke, setJoke] = React.useState('');
  const fetchJoke = async () => {
    try {
      const response = await fetch('http://localhost:5000/data', {
        method: 'GET',
        headers: {
          'X-RapidAPI-Key': 'your-api-key',
          'X-RapidAPI-Host': 'jokes-by-api-ninjas.p.rapidapi.com'
        }
      });
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const data = await response.json();
      setJoke(data);
      console.log((data))
    } catch (error) {
      console.error('Error:', error);
    }
  };
React.useEffect(() => {
    fetchJoke();
  }, []);
  return (
    <div>
      {joke}
    </div>
  );
}


export function ALprData() {
  const [ALprDataState, setAlprData] =  React.useState(null);
  React.useEffect(() => {
    fetch("http://localhost:5000/data", {
      method: "GET",
      headers: {
        "X-RapidAPI-Key": "your-api-key",
        "X-RapidAPI-Host": "jokes-by-api-ninjas.p.rapidapi.com",
      },
    })
      .then((response) => response.json())
      .then((data) => {
        setAlprData(data);
        data = JSON.parse(data)
        console.log((data[0]));
      })
      .catch((error) => console.log(error));
  }, []);
  return (
    <div>
      <h2>Joke of the day:</h2>
    </div>
  );
}