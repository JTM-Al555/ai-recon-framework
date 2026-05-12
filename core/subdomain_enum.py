import concurrent.futures
from typing import List

import httpx

from utils.logger import logger


COMMON_SUBDOMAINS = [
    "www",
    "mail",
    "api",
    "dev",
    "test",
    "admin",
    "vpn",
    "portal",
    "staging",
    "beta"
]


class SubdomainEnumerator:

    def __init__(self, domain: str):

        self.domain = domain

    def check_subdomain(
        self,
        subdomain: str
    ):

        url = f"https://{subdomain}.{self.domain}"

        try:
            response = httpx.get(
                url,
                timeout=3
            )

            return {
                "subdomain": url,
                "status": response.status_code
            }

        except Exception:
            return None

    def run(self) -> List:

        discovered = []

        with concurrent.futures.ThreadPoolExecutor(
            max_workers=20
        ) as executor:

            results = executor.map(
                self.check_subdomain,
                COMMON_SUBDOMAINS
            )

            for result in results:

                if result:
                    discovered.append(result)

        logger.info(
            f"Subdomain scan completed for {self.domain}"
        )

        return discovered