
from log_analyzer import LogAnalyzer

def test_mixed_status_codes():
    logs = [
        {"ip": "1.1.1.1", "status": 200},
        {"ip": "2.2.2.2", "status": 301},
        {"ip": "3.3.3.3", "status": 403},
        {"ip": "4.4.4.4", "status": 404},
        {"ip": "5.5.5.5", "status": 503}
    ]
    result = LogAnalyzer().analyze(logs)
    assert result["total_requests"] == 5
    assert result["error_count"] == 3
    assert result["error_rate"] == 60.0
