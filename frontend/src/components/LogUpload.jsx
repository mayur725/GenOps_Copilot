
import { analyzeLogs } from "../services/api";

export default function LogUpload({setData}){
  const submit=async(e)=>{
    const logs=e.target.value.split("\n");
    const res=await analyzeLogs(logs);
    setData(res);
  };
  return <textarea rows="6" placeholder="Paste logs here" onBlur={submit}/>;
}
