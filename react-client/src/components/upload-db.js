import React from "react"


const url = "http://172.187.216.226:5000/upload"
export default function DataTable() {
  const [items, setItems] = React.useState([]);
  React.useEffect(() => {
    fetch(url)
      .then((res) => res.json())
      .then((data) => setItems(data));
  }, []);
  console.log(items);
  const collection = items.map((plate, index) => {
    return (
        <li  key={index}>{plate}</li>
    );
  });
  return (
    <
    >
      {collection} {/* Render the collection of items */}
    </>
  );
}