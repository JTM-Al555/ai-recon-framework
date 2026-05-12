import asyncio

from rich.console import Console
from rich.table import Table

from ai.analyzer import AIAnalyzer
from ai.cve_mapper import CVEMapper

from core.async_scanner import AsyncPortScanner
from core.dns_enum import DNSEnumerator
from core.headers_analyzer import HeadersAnalyzer
from core.http_probe import HTTPProbe
from core.js_analyzer import JavaScriptAnalyzer
from core.screenshot import ScreenshotEngine
from core.ssl_analyzer import SSLAnalyzer
from core.subdomain_enum import SubdomainEnumerator
from core.tech_fingerprint import TechnologyFingerprinter
from core.web_crawler import WebCrawler
from core.whois_lookup import WhoisLookup

from output.html_reporter import HTMLReporter
from output.json_reporter import JSONReporter
from output.markdown_reporter import MarkdownReporter

from utils.banner import show_banner
from utils.helpers import validate_domain
from utils.logger import logger


console = Console()


async def run_framework(domain):

    logger.info(
        f"Starting recon for {domain}"
    )

    # DNS
    dns_results = (
        DNSEnumerator(domain).run()
    )

    # WHOIS
    whois_results = (
        WhoisLookup(domain).run()
    )

    # HTTP
    http_results = (
        HTTPProbe(domain).run()
    )

    # WEB CRAWLER
    crawl_results = await (
        WebCrawler(domain).crawl()
    )

    # JAVASCRIPT ANALYSIS
    js_results = await (
        JavaScriptAnalyzer(domain).run()
    )

    # SCREENSHOTS
    screenshots = await (
        ScreenshotEngine(domain).run()
    )

    # PORT SCAN
    ports = await (
        AsyncPortScanner(domain).run()
    )

    # SUBDOMAINS
    subdomains = (
        SubdomainEnumerator(domain).run()
    )

    # SSL
    ssl_data = (
        SSLAnalyzer(domain).run()
    )

    # HEADERS
    headers = (
        http_results.get(
            "headers",
            {}
        )
    )

    # SECURITY HEADERS
    header_analysis = (
        HeadersAnalyzer(
            headers
        ).analyze()
    )

    # TECHNOLOGIES
    technologies = (
        TechnologyFingerprinter(
            headers
        ).detect()
    )

    # CVE MAPPING
    cves = (
        CVEMapper(
            technologies
        ).map_cves()
    )

    # FINAL RESULTS
    results = {
        "dns": dns_results,
        "whois": whois_results,
        "http": http_results,
        "web_crawler": crawl_results,
        "javascript_analysis": js_results,
        "screenshots": screenshots,
        "ports": ports,
        "subdomains": subdomains,
        "ssl": ssl_data,
        "security_headers": (
            header_analysis
        ),
        "technologies": technologies,
        "cves": cves
    }

    # AI ANALYSIS
    ai_analysis = (
        AIAnalyzer(results).analyze()
    )

    results["ai_analysis"] = (
        ai_analysis
    )

    # REPORTS
    JSONReporter(
        domain,
        results
    ).save()

    MarkdownReporter(
        domain,
        results
    ).generate()

    HTMLReporter(
        domain,
        results
    ).generate()

    return results


def display_results(results):

    table = Table(
        title="Recon Summary"
    )

    table.add_column("Module")
    table.add_column("Status")

    for key in results.keys():

        table.add_row(
            key,
            "Completed"
        )

    console.print(table)


async def main():

    show_banner()

    domain = input(
        "Enter target domain: "
    ).strip()

    if not validate_domain(domain):

        console.print(
            "[red]Invalid domain[/red]"
        )

        return

    results = await run_framework(
        domain
    )

    display_results(results)

    console.print(
        "\n[green]Reports generated successfully.[/green]"
    )


if __name__ == "__main__":

    asyncio.run(main())