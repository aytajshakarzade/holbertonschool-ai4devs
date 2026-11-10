
from log_analyzer import LogAnalyzer

def test_invalid_input():
    result = LogAnalyzer().analyze("invalid")
    assert result["total_requests"] == 0
    assert result["unique_visitors"] == 0
    assert result["error_count"] == 0
