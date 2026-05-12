from datetime import datetime
from config.settings import OUTPUT_DIR


class MarkdownReporter:

    def __init__(self, domain, results):

        self.domain = domain
        self.results = results

    def generate_section(self, title, content):

        section = (
            "\n"
            f"## {title}\n\n"
            "```json\n"
            f"{content}\n"
            "```\n\n"
        )

        return section

    def generate(self):

        markdown = (
            "# AI Recon Report\n\n"
            f"Target:\n{self.domain}\n\n"
            f"Generated:\n{datetime.utcnow()}\n\n"
        )

        for key, value in self.results.items():

            markdown += self.generate_section(
                key,
                value
            )

        filename = (
            OUTPUT_DIR /
            f"{self.domain}.md"
        )

        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(markdown)

        return filename