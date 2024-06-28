import requests
import re

def extract_domain(url):
    domain_pattern = re.compile(r'^(?:https?|ftp)://([^/:]+)')
    match = domain_pattern.match(url)
    if match:
        return match.group(1)
    else:
        return None

url = input()
response = requests.get(url)
html_content = response.text

href_pattern = re.compile(r'<a\s+(?:[^>]*?\s+)?href="([^"]*)"')
hrefs = href_pattern.findall(html_content)

domains = set()
for href in hrefs:
    domain = extract_domain(href)
    if domain:
        domains.add(domain)

sorted_domains = sorted(domains)

for domain in sorted_domains:
    print(domain)
