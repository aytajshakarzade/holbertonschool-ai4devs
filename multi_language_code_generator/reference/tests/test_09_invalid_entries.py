
from log_analyzer import LogAnalyzer

def test_invalid_entries():
    logs = [
        {"ip": "1.1.1.1", "status": 200},
        "invalid",
        None,
        123
    ]
    result = LogAnalyzer().analyze(logs)
    assert result["total_requests"] == 1
