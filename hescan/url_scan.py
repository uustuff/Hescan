import requests

def scan_url(url, endpoints=None):
    if endpoints is None:
        endpoints = ["/admin", "/login", "/.git", "/.env", "/phpinfo.php"]
    print(f"[+] Scanning for vulnerable endpoints on {url}")
    for endpoint in endpoints:
        full_url = url.rstrip('/') + endpoint
        try:
            r = requests.get(full_url, timeout=4)
            if r.status_code == 200:
                print(f"Accessible: {full_url} [200]")
            elif r.status_code in (401, 403):
                print(f"Restricted: {full_url} [{r.status_code}]")
        except Exception as e:
            print(f"Error with {full_url}: {e}")

def deep_web_scan(url):
    # Example: checking for basic SQLi and XSS (expand as needed)
    payloads = {"sqli": "' OR '1'='1", "xss": "<script>alert(1)</script>"}
    print(f"[+] Deep scanning {url} for web vulns...")
    for attack, payload in payloads.items():
        try:
            resp = requests.get(url, params={"test": payload}, timeout=4)
            if attack == "sqli" and "sql" in resp.text.lower():
                print("Possible SQLi vulnerability detected!")
            if attack == "xss" and payload in resp.text:
                print("Possible XSS vulnerability detected!")
        except Exception as e:
            print(f"Web scan error: {e}")
