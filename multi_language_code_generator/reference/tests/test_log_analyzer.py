
import unittest

from log_analyzer import LogAnalyzer


class TestLogAnalyzer(unittest.TestCase):

    def setUp(self):
        self.analyzer = LogAnalyzer()

    def test_normal_requests(self):
        logs = [
            {"ip": "192.168.1.10", "status": 200},
            {"ip": "192.168.1.11", "status": 401},
            {"ip": "192.168.1.10", "status": 200}
        ]

        result = self.analyzer.analyze(logs)

        self.assertEqual(result["total_requests"], 3)
        self.assertEqual(result["unique_visitors"], 2)
        self.assertEqual(result["error_count"], 1)
        self.assertEqual(result["error_rate"], 33.33)

    def test_empty_input(self):
        result = self.analyzer.analyze([])

        self.assertEqual(result["total_requests"], 0)
        self.assertEqual(result["unique_visitors"], 0)
        self.assertEqual(result["error_count"], 0)
        self.assertEqual(result["error_rate"], 0.0)
        self.assertEqual(result["status_codes"], {})

    def test_duplicate_visitors(self):
        logs = [
            {"ip": "192.168.1.10", "status": 200},
            {"ip": "192.168.1.10", "status": 200},
            {"ip": "192.168.1.10", "status": 404},
            {"ip": "192.168.1.10", "status": 500}
        ]

        result = self.analyzer.analyze(logs)

        self.assertEqual(result["total_requests"], 4)
        self.assertEqual(result["unique_visitors"], 1)
        self.assertEqual(result["error_count"], 2)
        self.assertEqual(result["error_rate"], 50.0)

    def test_all_successful_requests(self):
        logs = [
            {"ip": "10.0.0.1", "status": 200},
            {"ip": "10.0.0.2", "status": 201},
            {"ip": "10.0.0.3", "status": 204}
        ]

        result = self.analyzer.analyze(logs)

        self.assertEqual(result["error_count"], 0)
        self.assertEqual(result["error_rate"], 0.0)

    def test_all_failed_requests(self):
        logs = [
            {"ip": "10.0.0.1", "status": 400},
            {"ip": "10.0.0.2", "status": 404},
            {"ip": "10.0.0.3", "status": 500}
        ]

        result = self.analyzer.analyze(logs)

        self.assertEqual(result["error_count"], 3)
        self.assertEqual(result["error_rate"], 100.0)

    def test_mixed_status_codes(self):
        logs = [
            {"ip": "10.0.0.1", "status": 200},
            {"ip": "10.0.0.2", "status": 301},
            {"ip": "10.0.0.3", "status": 403},
            {"ip": "10.0.0.4", "status": 404},
            {"ip": "10.0.0.5", "status": 503}
        ]

        result = self.analyzer.analyze(logs)

        self.assertEqual(result["total_requests"], 5)
        self.assertEqual(result["error_count"], 3)
        self.assertEqual(result["error_rate"], 60.0)

    def test_missing_ip_address(self):
        logs = [
            {"status": 200},
            {"ip": None, "status": 404},
            {"ip": "10.0.0.1", "status": 200}
        ]

        result = self.analyzer.analyze(logs)

        self.assertEqual(result["total_requests"], 3)
        self.assertEqual(result["unique_visitors"], 1)

    def test_invalid_status_codes_are_ignored(self):
        logs = [
            {"ip": "10.0.0.1", "status": 200},
            {"ip": "10.0.0.2", "status": 700},
            {"ip": "10.0.0.3", "status": "404"},
            {"ip": "10.0.0.4", "status": None}
        ]

        result = self.analyzer.analyze(logs)

        self.assertEqual(result["total_requests"], 1)
        self.assertEqual(result["error_count"], 0)

    def test_non_dictionary_entries_are_ignored(self):
        logs = [
            {"ip": "10.0.0.1", "status": 200},
            "invalid entry",
            None,
            123
        ]

        result = self.analyzer.analyze(logs)

        self.assertEqual(result["total_requests"], 1)

    def test_invalid_input_type(self):
        result = self.analyzer.analyze("invalid input")

        self.assertEqual(result["total_requests"], 0)
        self.assertEqual(result["unique_visitors"], 0)
        self.assertEqual(result["error_count"], 0)

    def test_status_code_grouping(self):
        logs = [
            {"ip": "10.0.0.1", "status": 200},
            {"ip": "10.0.0.2", "status": 200},
            {"ip": "10.0.0.3", "status": 404}
        ]

        result = self.analyzer.analyze(logs)

        self.assertEqual(
            result["status_codes"],
            {"200": 2, "404": 1}
        )

    def test_boolean_status_is_ignored(self):
        logs = [
            {"ip": "10.0.0.1", "status": True},
            {"ip": "10.0.0.2", "status": 200}
        ]

        result = self.analyzer.analyze(logs)

        self.assertEqual(result["total_requests"], 1)


if __name__ == "__main__":
    unittest.main()
