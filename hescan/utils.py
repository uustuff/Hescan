import re

def validate_ip(ip):
    pattern = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
    return re.match(pattern, ip) is not None

def validate_url(url):
    return url.startswith("http://") or url.startswith("https://")
