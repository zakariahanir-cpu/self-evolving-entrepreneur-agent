import json
import requests

class WebsiteInfiltrator:
    def __init__(self, vulnerabilities):
        self.vulnerabilities = vulnerabilities
        self.stolen_info = []

    def infiltrate_websites(self):
        for vulnerability in self.vulnerabilities:
            # Utilize the vulnerability to infiltrate the website and steal information
            href = vulnerability["href"]
            response = requests.get(href)

            if response.status_code == 200:
                self.stolen_info.append({
                    "href": href,
                    "info": response.text
                })

    def save_stolen_info(self, file_path):
        with open(file_path, 'w') as f:
            json.dump(self.stolen_info, f, indent=4)

# Example usage:
vulnerabilities = json.load(open("vulnerabilities.json", 'r'))
infiltrator = WebsiteInfiltrator(vulnerabilities)
infiltrator.infiltrate_websites()
infiltrator.save_stolen_info("stolen_info.json")