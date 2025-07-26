import nmap

def vulnerability_scan(target, ports):
    print(f"[+] Starting vulnerability scan on {target}:{ports} (Nmap required)")
    nm = nmap.PortScanner()
    port_str = ",".join(str(p) for p in ports)
    nm.scan(target, port_str, arguments='-sV --script vuln')
    for host in nm.all_hosts():
        print(f"\nHost: {host}")
        for proto in nm[host].all_protocols():
            lport = nm[host][proto].keys()
            for port in lport:
                print(f"Port: {port}")
                service = nm[host][proto][port].get("name")
                product = nm[host][proto][port].get("product", "")
                print(f"  Service: {service} ({product})")
                if 'script' in nm[host][proto][port]:
                    for script, output in nm[host][proto][port]['script'].items():
                        print(f"  {script}: {output}")
