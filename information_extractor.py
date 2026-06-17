import json
import re
from collections import deque

class InformationExtractor:
    def __init__(self, search_results):
        self.search_results = search_results
        self.extracted_info = []

    def extract_info(self):
        for result in self.search_results:
            # Extract title, href, and body from each search result
            title = re.search(r"title': '(.*?)'", result)
            href = re.search(r"href': '(.*?)'", result)
            body = re.search(r"body': '(.*?)'", result)

            if title and href and body:
                self.extracted_info.append({
                    "title": title.group(1),
                    "href": href.group(1),
                    "body": body.group(1)
                })

    def save_extracted_info(self, file_path):
        with open(file_path, 'w') as f:
            json.dump(self.extracted_info, f, indent=4)

# Example usage:
search_results = ["{'title': 'What does it take to defend the world against out-of-control AGIs?', 'href': 'https://www.lesswrong.com/posts/LFNXiQuGrar3duBzJ/what-does-it-take-to-defend-the-world-against-out-of-control', 'body': 'June 6, 2024 - Once China begins to truly unde'}"]
extractor = InformationExtractor(search_results)
extractor.extract_info()
extractor.save_extracted_info("extracted_info.json")