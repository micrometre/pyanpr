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
        <main className={`flex min-h-screen flex-col items-center justify-between p-24`}>
          <h2 className={`text-2xl font-semibold`}>
            <Alprd />
            <AlprdImages />
          </h2>
    </main>
    </>
  )
}