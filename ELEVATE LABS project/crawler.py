import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def is_valid_url(base_url, url):
    parsed_base = urlparse(base_url)
    parsed_url = urlparse(urljoin(base_url, url))
    return parsed_url.netloc == parsed_base.netloc

def crawl_website(start_url):
    visited_urls = set()
    urls_to_visit = [start_url]
    forms = []

    while urls_to_visit:
        url = urls_to_visit.pop(0)
        if url in visited_urls:
            continue

        visited_urls.add(url)
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')

            for link_tag in soup.find_all('a', href=True):
                link = urljoin(url, link_tag['href'])
                if is_valid_url(start_url, link) and link not in visited_urls:
                    urls_to_visit.append(link)

            for form in soup.find_all('form'):
                forms.append((url, form))

        except requests.exceptions.RequestException as e:
            print(f"[!] Failed to crawl {url}: {e}")
    
    return forms
