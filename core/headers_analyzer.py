from typing import Dict


SECURITY_HEADERS = [
    "Content-Security-Policy",
    "Strict-Transport-Security",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy"
]


class HeadersAnalyzer:

    def __init__(self, headers: Dict):

        self.headers = headers

    def analyze(self):

        analysis = {}

        for header in SECURITY_HEADERS:

            analysis[header] = {
                "present": header in self.headers,
                "value": self.headers.get(
                    header,
                    "Missing"
                )
            }

        return analysis