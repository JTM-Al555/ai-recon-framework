from typing import Dict, List

import dns.resolver

from config.settings import DNS_RECORD_TYPES
from utils.logger import logger


class DNSEnumerator:

    def __init__(self, domain: str):
        self.domain = domain

    def fetch_record(
        self,
        record_type: str
    ) -> List[str]:

        try:
            answers = dns.resolver.resolve(
                self.domain,
                record_type
            )

            return [str(answer) for answer in answers]

        except dns.resolver.NoAnswer:
            return ["No record found"]

        except dns.resolver.NXDOMAIN:
            return ["Domain does not exist"]

        except Exception as error:

            logger.error(
                f"DNS error ({record_type}): {error}"
            )

            return [f"Error: {error}"]

    def run(self) -> Dict[str, List[str]]:

        results = {}

        for record_type in DNS_RECORD_TYPES:

            results[record_type] = self.fetch_record(
                record_type
            )

        return results