
class LogAnalyzer:
    """Analyze server log entries and generate request statistics."""

    def analyze(self, entries):
        if not isinstance(entries, list):
            return self._empty_result()

        total_requests = 0
        error_count = 0
        unique_visitors = set()
        status_codes = {}

        for entry in entries:
            if not isinstance(entry, dict):
                continue

            status = entry.get("status")

            # Accept only valid HTTP status codes.
            if (
                not isinstance(status, int)
                or isinstance(status, bool)
                or status < 100
                or status > 599
            ):
                continue

            total_requests += 1

            ip = entry.get("ip")
            if isinstance(ip, str) and ip.strip():
                unique_visitors.add(ip.strip())

            status_key = str(status)
            status_codes[status_key] = (
                status_codes.get(status_key, 0) + 1
            )

            if 400 <= status <= 599:
                error_count += 1

        error_rate = (
            round((error_count / total_requests) * 100, 2)
            if total_requests > 0
            else 0.0
        )

        return {
            "total_requests": total_requests,
            "unique_visitors": len(unique_visitors),
            "error_count": error_count,
            "error_rate": error_rate,
            "status_codes": dict(sorted(status_codes.items()))
        }

    @staticmethod
    def _empty_result():
        return {
            "total_requests": 0,
            "unique_visitors": 0,
            "error_count": 0,
            "error_rate": 0.0,
            "status_codes": {}
        }


if __name__ == "__main__":
    sample_logs = [
        {"ip": "192.168.1.10", "status": 200},
        {"ip": "192.168.1.11", "status": 401},
        {"ip": "192.168.1.10", "status": 200},
        {"ip": "192.168.1.12", "status": 404},
        {"ip": "192.168.1.13", "status": 500}
    ]

    analyzer = LogAnalyzer()
    result = analyzer.analyze(sample_logs)

    import json
    print(json.dumps(result, indent=4))
