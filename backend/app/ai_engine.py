
def generate_root_cause(incident_logs):
    return "The incident is caused by repeated timeout failures in the service."

def generate_resolution(root_cause):
    return (
        "1.Restart the affected service\n"
        "2.Check network latency\n"
        "3.Scale application resources\n"
        "4.Monitor system logs"
    )
