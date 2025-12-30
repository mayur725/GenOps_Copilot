
from app.rules import detect_incidents
from app.ai_engine import generate_root_cause, generate_resolution

def process_logs(logs):
    incidents = detect_incidents(logs)
    if not incidents:
        return {
            "incident_logs": [],
            "root_cause": "No incident detected.",
            "resolution": "No action required."
        }
    rca = generate_root_cause(incidents)
    resolution = generate_resolution(rca)
    return {
        "incident_logs": incidents,
        "root_cause": rca,
        "resolution": resolution
    }
