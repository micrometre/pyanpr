import React from "react";
import fallback from "../logo.svg";

function onError(e) {
  e.target.src =
    "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/No_sign.svg/192px-No_sign.svg.png";
}

const testImg = "https://img.google.com/vi/some-random-id/maxresdefault.jpg";

export default function CameraImages({ src, alt, fallBackSrc = fallback.src }) {
  const [stateCameraImage, setCameraImage] = React.useState([]);
  React.useEffect(() => {
    const evtSource = new EventSource("http://172.187.216.226:5000/cameraimg");
    evtSource.onmessage = (event) => {
      const alprdImageData = JSON.parse(event.data)
      setCameraImage(alprdImageData)
    };
    evtSource.onopen = (event) => {
    };
  }, []);
  return (
    <>
        <main  >
        <div className="thumbnail">
          <div className="frame">
        <a href={stateCameraImage.img} target="_blank" rel="noopener noreferrer">
          <img
            src={stateCameraImage.img}
            alt={alt}
            onError={(e) => onError(e)}
            width="250" height="250"  
          />
        </a>
          </div>
        </div>
        <style>
          {`
            .thumbnail {
            }

            .frame {
              cursor: pointer;
            }

            .thumbnail img {
            }
        `}
        </style>

      </main>
    </>
  );
}

