import React from "react";
import AlprdImages from "./components/alprd-images";
import Alprd from "./components/alprd";
import SideNav from "./components/sidenav";
import AlprVideo from "./components/alprd-video";
export default function App() {
  return (
    <>
      <div className="flex h-screen flex-col md:flex-row md:overflow-hidden">
        <SideNav />
        <div className="grid gap-10 sm:grid-cols-2 lg:grid-cols-3">
          <Alprd />
          <AlprdImages />
          <AlprVideo />
        </div>
      </div>
    </>
  )
}