import React from "react";
import AlprdImages from "./components/alprd-images";
import Alprd from "./components/alprd";
import SideNav from "./components/sidenav";
import AlprVideo from "./components/alprd-video";
import AlprDb from "./components/alpr-db";
import { ArrowRightIcon } from '@heroicons/react/24/outline';
import { VideoCameraIcon } from '@heroicons/react/24/outline';

export default function App() {
  return (
    <>
      <main className={`flex flex-col items-center justify-between`}>
            <FileUpload />
            <br/>
            <AlprdImages />
            <Alprd />
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
    const response = await fetch("http://localhost:5000/upload", {
      method: "POST",
      body
    });
  };

  return (
    <div>
      <p>
        <input type="file" name="myImage" onChange={uploadToClient} />
      </p>
      <button type="submit" onClick={uploadToServer}
        className="mt-10 flex h-[48px] grow items-center justify-center gap-2 rounded-md bg-gray-50 p-3 text-sm font-medium hover:bg-sky-100 hover:text-blue-600 md:flex-none md:justify-start md:p-8 md:px-3"
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