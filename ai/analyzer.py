import json
from datetime import datetime


class AIAnalyzer:

    def __init__(self, results):

        self.results = results

    def analyze(self):

        """
        This is the "brain" of your framework.
        It converts raw recon data into insights.
        """

        insights = {
            "timestamp": str(datetime.utcnow()),
            "risk_score": 0,
            "summary": "",
            "findings": [],
            "recommendations": []
        }

        # -----------------------------
        # BASIC RISK LOGIC (simple AI)
        # -----------------------------

        risk = 0

        # DNS issues
        if self.results.get("dns"):
            risk += 1
            insights["findings"].append("DNS data collected")

        # Open ports
        ports = self.results.get("ports", [])
        if len(ports) > 5:
            risk += 3
            insights["findings"].append("Multiple open ports detected")
        elif len(ports) > 0:
            risk += 1
            insights["findings"].append("Some open ports detected")

        # HTTP issues
        if self.results.get("http"):
            insights["findings"].append("HTTP endpoint reachable")

        # Subdomains
        subdomains = self.results.get("subdomains", [])
        if len(subdomains) > 10:
            risk += 2
            insights["findings"].append("Large subdomain surface detected")

        # SSL check
        if self.results.get("ssl"):
            insights["findings"].append("SSL certificate info collected")

        # CVE check
        if self.results.get("cves"):
            risk += 3
            insights["findings"].append("Possible CVE matches found")

        # -----------------------------
        # FINAL SCORING
        # -----------------------------

        insights["risk_score"] = min(risk, 10)

        # -----------------------------
        # AI SUMMARY (VERY IMPORTANT)
        # -----------------------------

        if risk == 0:
            insights["summary"] = "Low risk target with minimal exposure."
        elif risk <= 3:
            insights["summary"] = "Low to moderate risk detected."
        elif risk <= 6:
            insights["summary"] = "Moderate risk with some exposure points."
        else:
            insights["summary"] = "High risk target with significant exposure."

        # -----------------------------
        # RECOMMENDATIONS
        # -----------------------------

        if risk > 5:
            insights["recommendations"].append("Review open ports and exposed services")
            insights["recommendations"].append("Check for unnecessary subdomains")
            insights["recommendations"].append("Harden SSL configuration")

        return insights


def run_ai_analysis(results):

    analyzer = AIAnalyzer(results)
    return analyzer.analyze()