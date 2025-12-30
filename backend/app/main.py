
from fastapi import FastAPI
from app.schemas import LogRequest, IncidentResponse
from app.processor import process_logs

app = FastAPI(title="GenOps Copilot")

@app.post("/analyze", response_model=IncidentResponse)
def analyze_logs(request: LogRequest):
    return process_logs(request.logs)
