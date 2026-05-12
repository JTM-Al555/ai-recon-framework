import json
from datetime import datetime


class PromptBuilder:

    @staticmethod
    def build(results):

        formatted_results = json.dumps(
            results,
            indent=2
        )

        return f"""
You are an expert cybersecurity analyst.

Analyze the reconnaissance results below.

Tasks:
1. Summarize findings
2. Identify attack surface
3. Mention risky technologies
4. Mention exposed services
5. Give security recommendations
6. Provide overall security assessment

Date:
{datetime.utcnow()}

Reconnaissance Results:
{formatted_results}
"""