from scapy.all import ARP, Ether, srp

def scan_network(target_ip):
    print(f"[+] Scanning network: {target_ip}")
    arp = ARP(pdst=target_ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp
    result = srp(packet, timeout=3, verbose=0)[0]
    hosts = []
    for sent, received in result:
        hosts.append({'ip': received.psrc, 'mac': received.hwsrc})
    print("IP\t\t\tMAC Address")
    print("-----------------------------------------")
    for host in hosts:
        print(f"{host['ip']}\t{host['mac']}")
    return hosts
