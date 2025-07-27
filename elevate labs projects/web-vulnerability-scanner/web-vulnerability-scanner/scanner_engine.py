import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

HEADERS = {"User-Agent": "Mozilla/5.0"}

def crawl_and_scan(base_url, limit=10):
    visited = set()
    queue = [base_url]
    vulnerabilities = []

    while queue and len(visited) < limit:
        url = queue.pop(0)
        if url in visited:
            continue

        visited.add(url)
        try:
            response = requests.get(url, headers=HEADERS, timeout=5)
            soup = BeautifulSoup(response.text, "html.parser")

            # 🔍 Check for vulnerabilities in forms
            for form in soup.find_all("form"):
                action = form.get("action")
                method = form.get("method", "get").lower()
                form_url = urljoin(url, action)
                inputs = [i.get("name") for i in form.find_all("input") if i.get("name")]

                for payload, attack in [("<script>alert(1)</script>", "XSS"), ("' OR '1'='1", "SQLi")]:
                    data = {name: payload for name in inputs}
                    try:
                        if method == "post":
                            r = requests.post(form_url, data=data, headers=HEADERS)
                        else:
                            r = requests.get(form_url, params=data, headers=HEADERS)

                        if payload in r.text:
                            vulnerabilities.append({
                                "url": form_url,
                                "type": attack,
                                "payload": payload,
                                "description": f"Possible {attack} via input on {form_url}",
                                "severity": "High" if attack == "SQLi" else "Medium"
                            })
                    except:
                        continue

            # 🔍 Check for missing headers
            if 'X-Frame-Options' not in response.headers:
                vulnerabilities.append({
                    "url": url,
                    "type": "Header",
                    "payload": "Missing X-Frame-Options",
                    "description": "Clickjacking protection header missing.",
                    "severity": "Low"
                })

            if 'Content-Security-Policy' not in response.headers:
                vulnerabilities.append({
                    "url": url,
                    "type": "Header",
                    "payload": "Missing Content-Security-Policy",
                    "description": "CSP header missing, XSS protection weakened.",
                    "severity": "Low"
                })

            # 🔁 Add new internal links to queue
            for a in soup.find_all("a", href=True):
                link = urljoin(url, a['href'])
                if base_url in link and link not in visited:
                    queue.append(link)

        except Exception as e:
            vulnerabilities.append({
                "url": url,
                "type": "Error",
                "payload": str(e),
                "description": f"Failed to scan {url}",
                "severity": "Info"
            })

    return list(visited), vulnerabilities
