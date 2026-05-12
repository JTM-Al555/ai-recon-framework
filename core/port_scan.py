import socket
from typing import List, Dict

from config.settings import (
    COMMON_PORTS,
    SOCKET_TIMEOUT
)

from utils.helpers import resolve_domain
from utils.logger import logger


class PortScanner:

    def __init__(self, domain: str):

        self.domain = domain
        self.ip = resolve_domain(domain)

    def scan_port(
        self,
        port: int
    ) -> bool:

        try:
            sock = socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM
            )

            sock.settimeout(SOCKET_TIMEOUT)

            result = sock.connect_ex(
                (self.ip, port)
            )

            sock.close()

            return result == 0

        except Exception as error:

            logger.error(
                f"Port scan error ({port}): {error}"
            )

            return False

    def run(self) -> List[Dict]:

        if not self.ip:

            return [{
                "error": "Could not resolve domain"
            }]

        open_ports = []

        for port, service in COMMON_PORTS.items():

            if self.scan_port(port):

                open_ports.append({
                    "port": port,
                    "service": service
                })

        return open_ports