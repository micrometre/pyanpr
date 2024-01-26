@@ -1,45 +0,0 @@
import React from "react"
import { useInterval } from "./useInterval";



export function useInterval(callback, delay) {	
    const savedCallback = React.useRef();	
    React.useEffect(() => {	
      savedCallback.current = callback;	
    }, [callback]);	
    React.useEffect(() => {	
      function tick() {	
        savedCallback.current();	
      }	
      if (delay !== null) {	
        let id = setInterval(tick, delay);	
        return () => clearInterval(id);	
      }	
    }, [delay]);	
  }	
  
export default function UploadDb() {
  const [data, setData] = React.useState(null);
  const [loading, setLoading] = React.useState(true);
  const [error, setError] = React.useState(null);
  useInterval(() => {
    async function fetchData() {
      setLoading(true);
      try {
        const response = await fetch('http://172.187.216.226:5000/uploaddb');
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const jsonData = await response.json();
        setData(jsonData);
        setError(null);
      } catch (error) {
        setError(error.message);
      } finally {
        setLoading(false);
      }
    }

    fetchData();
  }, 5000);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;
  const  revdata = data.reverse();
  console.log(revdata)
  const collection = data.map((plate, index) => {
    return (
        <li  key={index}>{plate}</li>
    );
  });
  return (
    <div>
      {collection} {/* Render the collection of items */}
    </div>
  );
}