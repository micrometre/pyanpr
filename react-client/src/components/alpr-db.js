import React, { useState } from "react";

export default function AlprDb() {
  const [state, setState] = React.useState([]);
  const [stateUuid, setUud] = React.useState([]);
  React.useEffect(() => {
    const evtSource = new EventSource("http://localhost:5000/data");
    evtSource.onmessage = (event) => {
    };
    evtSource.onopen = (event) => {
    };
  }, []);
    return (
        <>
        </>
    );
}
