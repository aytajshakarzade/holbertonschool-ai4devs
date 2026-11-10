
from log_analyzer import LogAnalyzer

def test_missing_ip():
    logs = [
        {"status": 200},
        {"ip": None, "status": 404},
        {"ip": "1.1.1.1", "status": 200}
    ]
    result = LogAnalyzer().analyze(logs)
    assert result["total_requests"] == 3
    assert result["unique_visitors"] == 1
