
export default function IncidentView({data}){
  if(!data) return null;
  return(
    <div>
      <h3>Incident Logs</h3>
      <pre>{data.incident_logs.join("\n")}</pre>
      <h3>Root Cause</h3>
      <p>{data.root_cause}</p>
      <h3>Resolution</h3>
      <pre>{data.resolution}</pre>
    </div>
  );
}
