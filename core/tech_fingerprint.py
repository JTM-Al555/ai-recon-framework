from typing import Dict


TECH_SIGNATURES = {
    "cloudflare": "Cloudflare",
    "nginx": "Nginx",
    "apache": "Apache",
    "php": "PHP",
    "express": "Express.js"
}


class TechnologyFingerprinter:

    def __init__(self, headers: Dict):

        self.headers = headers

    def detect(self):

        detected = []

        combined_headers = " ".join(
            [
                str(value).lower()
                for value in self.headers.values()
            ]
        )

        for signature, technology in (
            TECH_SIGNATURES.items()
        ):

            if signature in combined_headers:
                detected.append(technology)

        return detected