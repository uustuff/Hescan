from .banner import print_banner
from .network_scan import scan_network
from .wifi_scan import scan_wifi
from .port_scan import scan_ports
from .vuln_scan import vulnerability_scan
from .ip_lookup import lookup_ip
from .url_scan import scan_url, deep_web_scan

def main_menu():
    print_banner()
    while True:
        print("\n--- HeScan Main Menu ---")
        print("1. LAN Network Scan (Find live hosts)")
        print("2. WiFi Scanner")
        print("3. Port Scanner (Open Ports)")
        print("4. Vulnerability Scan (Nmap)")
        print("5. IP Lookup (Geo/info)")
        print("6. URL Scan (Endpoints/Web Vulns)")
        print("7. Exit")
        choice = input("Enter your choice [1-7]: ").strip()
        if choice == '1':
            iprange = input("Enter target IP/range (e.g. 192.168.1.0/24): ")
            scan_network(iprange)
        elif choice == '2':
            scan_wifi()
        elif choice == '3':
            target = input("Enter target IP/hostname: ").strip()
            min_port = int(input("Min port (default 1): ") or 1)
            max_port = int(input("Max port (default 1024): ") or 1024)
            scan_ports(target, (min_port, max_port))
        elif choice == '4':
            target = input("Enter target IP/hostname: ").strip()
            min_port = int(input("Min port (default 1): ") or 1)
            max_port = int(input("Max port (default 1024): ") or 1024)
            ports = list(range(min_port, max_port+1))
            vulnerability_scan(target, ports)
        elif choice == '5':
            ip = input("Enter IP to lookup: ").strip()
            lookup_ip(ip)
        elif choice == '6':
            url = input("Enter full URL: ").strip()
            scan_url(url)
            deep = input("Deep scan for web vulns (y/n)? ").strip().lower()
            if deep == 'y':
                deep_web_scan(url)
        elif choice == '7':
            print("Goodbye from HeScan!")
            break
        else:
            print("Invalid choice, please select 1-7.")
