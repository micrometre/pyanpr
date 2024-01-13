import React from "react";
import AlprdImages from "./components/alprd-images";
import Alprd from "./components/alprd";
import AlprVideo from "./components/alprd-video";
import UploadDb from "./components/upload-db";
import CameraImages from "./components/camera-images";
import { ArrowRightIcon } from '@heroicons/react/24/outline';
import { VideoCameraIcon } from '@heroicons/react/24/outline';
import { FileUpload } from "./components/FileUpload";

export default function App() {
  return (
    <>
      <main className={`flex flex-col items-center justify-between`}>
        <AlprdImages />
        <FileUpload />
        <UploadDb />
      </main>
    </>
  )
}


