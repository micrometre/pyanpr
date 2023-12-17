import React from "react";
import AlprdImages from "./components/alprd-images";
import Alprd from "./components/alprd";
import './App.css';
import ReactPlaceholder from 'react-placeholder';
import "react-placeholder/lib/reactPlaceholder.css";

export default function App() {
  return (
    <>
      <AlprdImages />
      <Alprd />
    </>
  )
}