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
      <Alprd />
      <AlprdImages />
    </>
  )
}