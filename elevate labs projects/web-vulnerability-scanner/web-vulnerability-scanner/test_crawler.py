import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

visited = set()
base_url = "http://testphp.vulnweb.com"
headers = {"User-Agent": "Mozilla/5.0"}

try:
    response = requests.get(base_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    for a in soup.find_all("a", href=True):
        full = urljoin(base_url, a["href"])
        if base_url in full and full not in visited:
            visited.add(full)
            print(full)

    print(f"\nTotal links found: {len(visited)}")

except Exception as e:
    print("Error:", str(e))
