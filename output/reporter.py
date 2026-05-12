# output/reporter.py

import json
from datetime import datetime

def save_report(data, filename="report.json"):
    """
    Saves structured recon report with timestamp.
    """

    data["timestamp"] = str(datetime.now())

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

    print(f"[+] Report saved → {filename}")