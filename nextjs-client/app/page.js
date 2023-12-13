"use client";

import { FC, useEffect, useMemo, useState } from "react";


export default function Home() {
  const [state, setState] = useState([]);

  useEffect(() => {
    const evtSource = new EventSource("http://localhost:5000/alprdsse");
    evtSource.onmessage = (event) => {
      const myEvent = JSON.parse(event.data);
      console.log(myEvent);
      setState(myEvent);
    };

    evtSource.onopen = (event) => {
      console.log(event);
    };

    evtSource.onerror = () => {
      evtSource.close();
    };

    return function () {
      evtSource.close();
    };
  }, []);
  return (
    <div>
      <p>{state.uuid}</p>
      <p>{state.epoch_time}</p>

    </div>
  );
}
