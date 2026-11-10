
from log_analyzer import LogAnalyzer

def test_duplicate_visitors():
    logs = [
        {"ip": "1.1.1.1", "status": 200},
        {"ip": "1.1.1.1", "status": 404},
        {"ip": "1.1.1.1", "status": 500}
    ]
    result = LogAnalyzer().analyze(logs)
    assert result["unique_visitors"] == 1
    assert result["error_count"] == 2
