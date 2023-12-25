import React from "react";
import fallback from "../logo.svg";

export default function AlprdImages({ src, alt, fallBackSrc = fallback.src }) {
  const [stateImage, setImage] = React.useState([]);
  React.useEffect(() => {
    const evtSource = new EventSource("http://localhost:5000/images");
    evtSource.onmessage = (event) => {
      const alprdImageData = JSON.parse(event.data)
      setImage(alprdImageData)
    };
    evtSource.onopen = (event) => {
    };
  }, []);
  return (
    <>
      <main className="flex flex-col items-center justify-between" >
        <div className="thumbnail">
          <div className="frame">
            <img
              src={stateImage.img}
              alt={alt}
              onError={(e) => (e.currentTarget.src = fallBackSrc)}
            />
            <h2 className="font-semibold">
              {stateImage.img}
            </h2>
            <a href={stateImage.img} target="_blank"
              rel="noopener noreferrer"
            >
            </a>
          </div>
        </div>
        <style>
          {`
            .thumbnail {
            }

            .frame {
                cursor: pointer;
                overflow: hidden;
            }

            .thumbnail img {
                width: 55%;
                height: 55%;
            }
        `}
        </style>

      </main>




    </>
  );
}

