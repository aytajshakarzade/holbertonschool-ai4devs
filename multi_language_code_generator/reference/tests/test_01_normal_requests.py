
from log_analyzer import LogAnalyzer

def test_normal_requests():
    result = LogAnalyzer().analyze([
        {"ip": "1.1.1.1", "status": 200},
        {"ip": "2.2.2.2", "status": 401},
        {"ip": "1.1.1.1", "status": 200}
    ])
    assert result["total_requests"] == 3
    assert result["unique_visitors"] == 2
    assert result["error_count"] == 1
    assert result["error_rate"] == 33.33
