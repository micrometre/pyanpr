import React from "react";
import AlprdImages from "./components/alprd-images";
import Alprd from "./components/alprd";
import AlprVideo from "./components/alprd-video";
import UploadDb from "./components/upload-db";
import CameraImages from "./components/camera-images";
import { ArrowRightIcon } from '@heroicons/react/24/outline';
import { VideoCameraIcon } from '@heroicons/react/24/outline';
import axios from 'axios';

export default function App() {
  return (
    <>
      <main className={`flex flex-col items-center justify-between`}>
            <UploadDb/>
            <br/>
            <Alprd />
            <AlprdImages />
            <FileUpload />
      </main>
    </>
  )
}


export function FileUpload(props) {
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
      <p>
        <input type="file" name="myImage"  accept="image/*"  onChange={uploadToClient} />
        {image ? <img src={createObjectURL} className="image" alt="preview" /> : null}

      </p>
      <button type="submit" onClick={uploadToServer}
      >
        <br />
        <p>
          Send Video file to server
        </p>
        <VideoCameraIcon className="mr-4" />
      </button>
    </div>
  );
}