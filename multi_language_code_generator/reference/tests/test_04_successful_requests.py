
from log_analyzer import LogAnalyzer

def test_successful_requests():
    logs = [
        {"ip": "1.1.1.1", "status": 200},
        {"ip": "2.2.2.2", "status": 201},
        {"ip": "3.3.3.3", "status": 204}
    ]
    result = LogAnalyzer().analyze(logs)
    assert result["error_count"] == 0
    assert result["error_rate"] == 0.0
