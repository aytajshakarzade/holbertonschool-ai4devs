
from log_analyzer import LogAnalyzer

def test_empty_input():
    result = LogAnalyzer().analyze([])
    assert result["total_requests"] == 0
    assert result["unique_visitors"] == 0
    assert result["error_count"] == 0
    assert result["error_rate"] == 0.0
