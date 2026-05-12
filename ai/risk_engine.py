from typing import Dict, List


class RiskEngine:

    HIGH_RISK_PORTS = {
        21: "FTP",
        23: "TELNET",
        25: "SMTP",
        3306: "MYSQL"
    }

    def __init__(self, results: Dict):

        self.results = results

    def analyze_ports(self) -> int:

        score = 0

        ports = self.results.get(
            "ports",
            []
        )

        for item in ports:

            if not isinstance(item, dict):
                continue

            port = item.get("port")

            if port in self.HIGH_RISK_PORTS:
                score += 20

        return score

    def analyze_headers(self) -> int:

        score = 0

        headers = self.results.get(
            "security_headers",
            {}
        )

        for _, data in headers.items():

            if not data.get("present"):
                score += 5

        return score

    def analyze_ssl(self) -> int:

        ssl_data = self.results.get(
            "ssl",
            {}
        )

        if ssl_data.get("valid") is False:
            return 20

        return 0

    def calculate(self):

        total_score = 0

        total_score += self.analyze_ports()
        total_score += self.analyze_headers()
        total_score += self.analyze_ssl()

        severity = self.get_severity(
            total_score
        )

        return {
            "score": total_score,
            "severity": severity
        }

    @staticmethod
    def get_severity(score):

        if score >= 70:
            return "HIGH"

        if score >= 40:
            return "MEDIUM"

        return "LOW"