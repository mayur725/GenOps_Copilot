
import { useState } from "react";
import LogUpload from "./components/LogUpload";
import IncidentView from "./components/IncidentView";

export default function App(){
  const [data,setData]=useState(null);
  return(
    <div>
      <h1>GenOps Copilot</h1>
      <LogUpload setData={setData}/>
      <IncidentView data={data}/>
    </div>
  );
}
