import React from "react";
import AlprdImages from "./components/alprd-images";
import Alprd from "./components/alprd";
import SideNav from "./components/sidenav";
export default function App() {
  return (
    <>
      <div className="flex h-screen flex-col md:flex-row md:overflow-hidden">
        <div className="w-full flex-none md:w-64">
          <SideNav />
        </div>
        <div className="grid gap-10 sm:grid-cols-2 lg:grid-cols-2">
          <Alprd />
          <AlprdImages />
        </div>
      </div>
    </>
  )
}