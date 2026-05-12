import asyncio
from urllib.parse import urljoin

import httpx
from bs4 import BeautifulSoup

from utils.logger import logger


COMMON_PATHS = [
    "/",
    "/login",
    "/admin",
    "/dashboard",
    "/api",
    "/robots.txt",
    "/sitemap.xml",
    "/graphql",
    "/auth",
    "/register"
]


class WebCrawler:

    def __init__(
        self,
        domain
    ):

        self.domain = domain

        self.base_url = (
            f"https://{domain}"
        )

        self.discovered = []

    async def fetch(
        self,
        client,
        path
    ):

        url = urljoin(
            self.base_url,
            path
        )

        try:

            response = await client.get(
                url
            )

            logger.info(
                f"Fetched {url}"
            )

            return {
                "url": url,
                "status": (
                    response.status_code
                ),
                "content_length": len(
                    response.text
                )
            }

        except Exception as error:

            logger.warning(
                f"Crawler error: {error}"
            )

            return None

    async def crawl(self):

        async with httpx.AsyncClient(
            timeout=10,
            follow_redirects=True
        ) as client:

            tasks = []

            for path in COMMON_PATHS:

                tasks.append(
                    self.fetch(
                        client,
                        path
                    )
                )

            results = await asyncio.gather(
                *tasks
            )

            for result in results:

                if result:
                    self.discovered.append(
                        result
                    )

        return self.discovered