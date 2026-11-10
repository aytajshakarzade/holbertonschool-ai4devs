
from log_analyzer import LogAnalyzer

def test_invalid_status():
    logs = [
        {"ip": "1.1.1.1", "status": 700},
        {"ip": "2.2.2.2", "status": "404"},
        {"ip": "3.3.3.3", "status": 200}
    ]
    result = LogAnalyzer().analyze(logs)
    assert result["total_requests"] == 1
