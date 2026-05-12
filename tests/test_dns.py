from core.dns_enum import DNSEnumerator


def test_dns():

    scanner = DNSEnumerator(
        "example.com"
    )

    results = scanner.run()

    assert isinstance(
        results,
        dict
    )