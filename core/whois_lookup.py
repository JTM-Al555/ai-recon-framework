from typing import Dict

import whois

from utils.logger import logger


class WhoisLookup:

    def __init__(self, domain):

        self.domain = domain

    def run(self) -> Dict:

        try:
            data = whois.whois(
                self.domain
            )

            return {
                "domain_name": (
                    data.domain_name
                ),
                "registrar": (
                    data.registrar
                ),
                "creation_date": str(
                    data.creation_date
                ),
                "expiration_date": str(
                    data.expiration_date
                ),
                "name_servers": str(
                    data.name_servers
                ),
                "emails": str(
                    data.emails
                )
            }

        except Exception as error:

            logger.error(
                f"WHOIS lookup failed: {error}"
            )

            return {
                "error": str(error)
            }