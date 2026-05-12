import re
import socket


DOMAIN_REGEX = re.compile(
    r"^(?:[a-zA-Z0-9]"
    r"(?:[a-zA-Z0-9-]{0,61}"
    r"[a-zA-Z0-9])?\.)"
    r"+[a-zA-Z]{2,}$"
)


def validate_domain(domain: str) -> bool:
    return DOMAIN_REGEX.match(domain) is not None


def resolve_domain(domain: str):

    try:
        return socket.gethostbyname(domain)

    except socket.gaierror:
        return None