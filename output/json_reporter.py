import json
from datetime import datetime

from config.settings import (
    OUTPUT_DIR
)


class JSONReporter:

    def __init__(
        self,
        domain,
        results
    ):

        self.domain = domain
        self.results = results

    def build_payload(self):

        return {
            "target": self.domain,
            "generated_at": str(
                datetime.utcnow()
            ),
            "results": self.results
        }

    def save(self):

        filename = (
            OUTPUT_DIR /
            f"{self.domain}.json"
        )

        payload = self.build_payload()

        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                payload,
                file,
                indent=4
            )

        return filename