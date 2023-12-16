import React from "react";


export default function AlprdImages() {
  const [stateImage, setImage] = React.useState([]);
  React.useEffect(() => {
    const evtSource = new EventSource("http://localhost:5000/images");
    evtSource.onmessage = (event) => {
      const alprdImageData = JSON.parse(event.data)
      console.log(alprdImageData);
      setImage(alprdImageData)
    };
    evtSource.onopen = (event) => {
      console.log(event);
    };
  }, []);
  return (
    <>
<h1 className="text-3xl font-bold underline">
  {stateImage.img}
</h1>
<img src={stateImage.img} alt="Alprd Imges"   />;
    </>
  );
}

