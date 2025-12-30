
export async function analyzeLogs(logs){
  const res=await fetch("http://localhost:8000/analyze",{
    method:"POST",
    headers:{"Content-Type":"application/json"},
    body:JSON.stringify({logs})
  });
  return res.json();
}
