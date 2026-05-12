from pathlib import Path

from config.settings import OUTPUT_DIR


class HTMLReporter:

    def __init__(
        self,
        domain,
        results
    ):

        self.domain = domain
        self.results = results

    def build_section(
        self,
        title,
        content
    ):

        return f"""
        <div class="section">
            <h2>{title}</h2>
            <pre>{content}</pre>
        </div>
        """

    def generate(self):

        sections = ""

        for key, value in self.results.items():

            sections += self.build_section(
                key,
                value
            )

        html = f"""
        <!DOCTYPE html>
        <html>

        <head>
            <title>Recon Report</title>

            <style>

                body {{
                    background-color: #0f172a;
                    color: #e2e8f0;
                    font-family: Arial;
                    padding: 30px;
                }}

                .section {{
                    background: #1e293b;
                    padding: 20px;
                    margin-bottom: 20px;
                    border-radius: 10px;
                }}

                h1 {{
                    color: #38bdf8;
                }}

                h2 {{
                    color: #22c55e;
                }}

                pre {{
                    white-space: pre-wrap;
                }}

            </style>

        </head>

        <body>

            <h1>
                AI Recon Report:
                {self.domain}
            </h1>

            {sections}

        </body>

        </html>
        """

        filename = (
            OUTPUT_DIR /
            f"{self.domain}.html"
        )

        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(html)

        return filename