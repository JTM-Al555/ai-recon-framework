from core.port_scan import PortScanner


def test_ports():

    scanner = PortScanner(
        "example.com"
    )

    results = scanner.run()

    assert isinstance(
        results,
        list
    )