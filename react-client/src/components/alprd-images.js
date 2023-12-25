import React from "react";
import fallback from "../logo.svg";

function onError(e) {
  e.target.src =
    "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/No_sign.svg/2048px-No_sign.svg.png";
}

const testImg = "https://img.google.com/vi/some-random-id/maxresdefault.jpg";

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
        <div className="rounded-xl bg-gray-50 p-2 shadow-sm">
          <div className="flex p-4">
            <div className="thumbnail">
              <div className="frame">
                <img
                  src={stateImage.img}
                  alt={alt}
                  onError={(e) => onError(e)}
                />
                <h2 className="font-semibold">
                </h2>
                <a href={stateImage.img} target="_blank"
                  rel="noopener noreferrer"
                >
                </a>
              </div>
            </div>
          </div>
        </div>

        <style>
          {`
            .frame {
                cursor: pointer;
                overflow: hidden;
            }
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

