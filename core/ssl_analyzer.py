import socket
import ssl
from datetime import datetime


class SSLAnalyzer:

    def __init__(self, domain: str):

        self.domain = domain

    def run(self):

        try:
            context = ssl.create_default_context()

            with socket.create_connection(
                (self.domain, 443)
            ) as sock:

                with context.wrap_socket(
                    sock,
                    server_hostname=self.domain
                ) as secure_sock:

                    cert = secure_sock.getpeercert()

                    return {
                        "issuer": cert.get("issuer"),
                        "subject": cert.get("subject"),
                        "expires": cert.get("notAfter"),
                        "valid": self.is_valid(
                            cert.get("notAfter")
                        )
                    }

        except Exception as error:

            return {
                "error": str(error)
            }

    def is_valid(self, expiry_date):

        try:
            expiry = datetime.strptime(
                expiry_date,
                "%b %d %H:%M:%S %Y %Z"
            )

            return expiry > datetime.utcnow()

        except Exception:
            return False