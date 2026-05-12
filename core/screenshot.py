import os
from pathlib import Path

from playwright.async_api import async_playwright

from utils.logger import logger


class ScreenshotEngine:

    def __init__(self, domain):

        self.domain = domain

        self.output_dir = (
            Path("output/screenshots")
        )

        self.output_dir.mkdir(
            parents=True,
            exist_ok=True
        )

    async def capture(self, url):

        filename = (
            url.replace("https://", "")
            .replace("http://", "")
            .replace("/", "_")
        )

        screenshot_path = (
            self.output_dir /
            f"{filename}.png"
        )

        try:

            async with async_playwright() as p:

                browser = await (
                    p.chromium.launch(
                        headless=True
                    )
                )

                page = await browser.new_page()

                await page.goto(
                    url,
                    timeout=15000
                )

                await page.screenshot(
                    path=str(
                        screenshot_path
                    ),
                    full_page=True
                )

                await browser.close()

                logger.info(
                    f"Screenshot saved: {url}"
                )

                return str(
                    screenshot_path
                )

        except Exception as error:

            logger.warning(
                f"Screenshot failed: {error}"
            )

            return None

    async def run(self):

        targets = [
            f"https://{self.domain}",
            f"http://{self.domain}"
        ]

        screenshots = []

        for target in targets:

            result = await self.capture(
                target
            )

            if result:
                screenshots.append(
                    result
                )

        return screenshots