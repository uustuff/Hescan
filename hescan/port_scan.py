import socket

def scan_ports(target, port_range=(1, 1024)):
    print(f"[+] Scanning {target} for open ports...")
    open_ports = []
    for port in range(port_range[0], port_range[1]+1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.5)
            result = sock.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)
                print(f"Port {port} is open")
    if not open_ports:
        print("No open ports found.")
    return open_ports
