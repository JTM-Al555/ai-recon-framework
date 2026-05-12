from core.http_probe import HTTPProbe


def test_http():

    scanner = HTTPProbe(
        "example.com"
    )

    results = scanner.run()

    assert isinstance(
        results,
        dict
    )