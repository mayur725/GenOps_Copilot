
ERROR_KEYWORDS = ["ERROR", "FAIL", "Timeout", "Exception"]

def detect_incidents(logs):
    return [log for log in logs if any(k in log for k in ERROR_KEYWORDS)]
