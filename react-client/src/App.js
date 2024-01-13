import React from "react";
import AlprdImages from "./components/alprd-images";
import Alprd from "./components/alprd";
import AlprVideo from "./components/alprd-video";
import UploadDb from "./components/upload-db";
import CameraImages from "./components/camera-images";
import { ArrowRightIcon } from '@heroicons/react/24/outline';
import { VideoCameraIcon } from '@heroicons/react/24/outline';

export default function App() {
  return (
    <>
      <main className={`flex flex-col items-center justify-between`}>
        <AlprdImages />
        <Alprd />
      </main>
      <main className={`flex flex-col items-center justify-between`}>
        <FileUpload />
        <UploadDb />
      </main>
    </>
  )
}


export function FileUpload(props) {
  const ImageStyle = { width: '250px', height: '300px' };

  const [image, setImage] = React.useState(null);
  const [createObjectURL, setCreateObjectURL] = React.useState(null);

  const uploadToClient = (event) => {
    if (event.target.files && event.target.files[0]) {
      const i = event.target.files[0];

      setImage(i);
      setCreateObjectURL(URL.createObjectURL(i));
    }
  };

  const uploadToServer = async (event) => {
    const body = new FormData();
    body.append("file", image);
    const response = await fetch("http://172.187.216.226:5000/upload", {
      method: "POST",
      body
    });
  };

  return (
    <div>
        <input type="file" name="myImage" accept="image/*" onChange={uploadToClient} />
        {image ? <img src={createObjectURL} style={ImageStyle} className="image" alt="preview" /> : null}
      <button type="submit" onClick={uploadToServer}>
        <h2 className={`mb-3 text-2xl font-semibold`}>
          Send  file to server
        </h2>
      </button>
    </div>
  );
}