
from log_analyzer import LogAnalyzer

def test_failed_requests():
    logs = [
        {"ip": "1.1.1.1", "status": 400},
        {"ip": "2.2.2.2", "status": 404},
        {"ip": "3.3.3.3", "status": 500}
    ]
    result = LogAnalyzer().analyze(logs)
    assert result["error_count"] == 3
    assert result["error_rate"] == 100.0
