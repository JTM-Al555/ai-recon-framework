CVE_DATABASE = {
    "Apache": [
        "Example CVE: CVE-2021-41773"
    ],

    "PHP": [
        "Example CVE: CVE-2019-11043"
    ],

    "Nginx": [
        "Example CVE: CVE-2021-23017"
    ]
}


class CVEMapper:

    def __init__(
        self,
        technologies
    ):

        self.technologies = technologies

    def map_cves(self):

        results = {}

        for tech in self.technologies:

            if tech in CVE_DATABASE:

                results[tech] = (
                    CVE_DATABASE[tech]
                )

        return results