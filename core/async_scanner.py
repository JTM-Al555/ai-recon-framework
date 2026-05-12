import asyncio
from typing import List, Dict

from config.settings import COMMON_PORTS
from utils.helpers import resolve_domain
from utils.logger import logger


class AsyncPortScanner:

    def __init__(self, domain: str):

        self.domain = domain
        self.ip = resolve_domain(domain)

    async def scan_port(
        self,
        port: int,
        service: str
    ):

        try:
            reader, writer = await asyncio.wait_for(
                asyncio.open_connection(
                    self.ip,
                    port
                ),
                timeout=1
            )

            writer.close()
            await writer.wait_closed()

            return {
                "port": port,
                "service": service,
                "status": "open"
            }

        except Exception:
            return None

    async def run(self) -> List[Dict]:

        if not self.ip:
            return [{
                "error": "Could not resolve domain"
            }]

        tasks = []

        for port, service in COMMON_PORTS.items():

            tasks.append(
                self.scan_port(port, service)
            )

        results = await asyncio.gather(*tasks)

        open_ports = [
            result for result in results
            if result is not None
        ]

        logger.info(
            f"Async scan completed for {self.domain}"
        )

        return open_ports