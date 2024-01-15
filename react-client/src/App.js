import React from "react";
import AlprdImages from "./components/alprd-images";
import Alprd from "./components/alprd";
import AlprVideo from "./components/alprd-video";
import UploadDb from "./components/upload-db";
import { ArrowRightIcon } from '@heroicons/react/24/outline';
import { VideoCameraIcon } from '@heroicons/react/24/outline';
import { FileUpload } from "./components/FileUpload";
import { VideoUpload } from "./components/VideoUpload";
import { ArrowPathIcon, CloudArrowUpIcon, FingerPrintIcon, LockClosedIcon } from '@heroicons/react/24/outline'




const people = [
  {
    name: 'Leslie Alexander',
    role: 'Co-Founder / CEO',
    imageUrl:
      'https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
  },
  // More people...
]

export default function Example() {
  return (
    <div className="bg-white py-24 sm:py-32">
      <div className="mx-auto grid max-w-7xl gap-x-2 gap-y-2 px-6 lg:px-8 xl:grid-cols-2">
        <div className="max-w-2xl">
        <FileUpload />
        <UploadDb />
        </div>

        <div className="max-w-2xl">
        <VideoUpload />
        </div>
      </div>

        <div style={{
           width:200,

           position: "fixed",
           bottom:30,
           right:150
        }}>

        <Alprd/>
        </div>


      
      <div style={{
           width:200,
           position: "fixed",
           bottom:30,
           right:0
        }}>
        <AlprdImages />
        </div>
    </div>
  )
}




export function App() {
  return (
    <>
      <main className={`flex`}>
        <FileUpload/>
        <VideoUpload/>





        
        <div style={{
           width:200,

           position: "fixed",
           bottom:30,
           right:150
        }}>

        <Alprd/>
        </div>
        <div style={{
           width:200,
           position: "fixed",
           bottom:30,
           right:0
        }}>
        <AlprdImages />
        </div>
      </main>
    </>
  )
}







