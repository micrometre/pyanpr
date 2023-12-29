import React from "react";
import AlprdImages from "./components/alprd-images";
import Alprd from "./components/alprd";
import SideNav from "./components/sidenav";
import AlprVideo from "./components/alprd-video";
import AlprDb from "./components/alpr-db";
import { ArrowRightIcon } from '@heroicons/react/24/outline';

export default function App() {
  return (
    <>
      <SideNav />
      <main className={`flex min-h-screen flex-col items-center justify-between`}>
        <div className="grid grid-cols-2 gap-1">
          <div>01
            <Alprd />
          </div>
          <div>
            <AlprdImages />
          </div>
          <div>
          </div>
        </div>
            <AlprDb />
      </main>
    </>
  )
}