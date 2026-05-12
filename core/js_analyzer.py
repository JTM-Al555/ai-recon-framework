import asyncio
import re
from urllib.parse import urljoin

import httpx
from bs4 import BeautifulSoup

from utils.logger import logger


ENDPOINT_REGEX = re.compile(
    r"""(?:"|')(
    \/api\/[a-zA-Z0-9_\-/]+|
    https?:\/\/[^\s"'<>]+
    )(?:"|')""",
    re.VERBOSE
)


class JavaScriptAnalyzer:

    def __init__(self, domain):

        self.domain = domain

        self.base_url = (
            f"https://{domain}"
        )

        self.discovered_files = []
        self.discovered_endpoints = []

    async def fetch_html(self):

        try:

            async with httpx.AsyncClient(
                timeout=10,
                follow_redirects=True
            ) as client:

                response = await client.get(
                    self.base_url
                )

                return response.text

        except Exception as error:

            logger.error(
                f"HTML fetch error: {error}"
            )

            return None

    def extract_js_files(
        self,
        html
    ):

        soup = BeautifulSoup(
            html,
            "html.parser"
        )

        scripts = soup.find_all(
            "script"
        )

        for script in scripts:

            src = script.get("src")

            if src:

                full_url = urljoin(
                    self.base_url,
                    src
                )

                if (
                    full_url
                    not in self.discovered_files
                ):

                    self.discovered_files.append(
                        full_url
                    )

    async def analyze_js_file(
        self,
        client,
        js_url
    ):

        try:

            response = await client.get(
                js_url
            )

            matches = (
                ENDPOINT_REGEX.findall(
                    response.text
                )
            )

            cleaned_matches = list(
                set(matches)
            )

            logger.info(
                f"Analyzed JS file: {js_url}"
            )

            return {
                "file": js_url,
                "endpoints": cleaned_matches
            }

        except Exception as error:

            logger.warning(
                f"JS analysis failed: {error}"
            )

            return None

    async def run(self):

        html = await self.fetch_html()

        if not html:

            return {
                "error": (
                    "Could not fetch target HTML"
                )
            }

        self.extract_js_files(
            html
        )

        async with httpx.AsyncClient(
            timeout=10,
            follow_redirects=True
        ) as client:

            tasks = []

            for js_file in (
                self.discovered_files
            ):

                tasks.append(
                    self.analyze_js_file(
                        client,
                        js_file
                    )
                )

            results = await asyncio.gather(
                *tasks
            )

        cleaned_results = []

        for result in results:

            if result:
                cleaned_results.append(
                    result
                )

        return cleaned_results