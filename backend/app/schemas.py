
from pydantic import BaseModel
from typing import List

class LogRequest(BaseModel):
    logs: List[str]

class IncidentResponse(BaseModel):
    incident_logs: List[str]
    root_cause: str
    resolution: str
