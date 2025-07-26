# HeScan

**HeScan** is a modular, multi-function network reconnaissance and vulnerability analysis tool. With live host discovery, WiFi scanning, deep port and web vulnerability scans, IP lookups, and more, HeScan is your versatile command-line Swiss Army knife for security tasks.

## 🚩 Features

- **Random Banner Art**: Displays a unique hacker-style ASCII banner on each run.
- **LAN Network Scanner**: Detects live hosts on your local network using ARP scanning.
- **WiFi Scanner**: Lists visible WiFi networks (supports major OSes).
- **Port Scanner**: Searches single or ranges of ports for open states, fast and customizable.
- **Vulnerability Scanner**: Integrates with Nmap for deep service and vulnerability checks.
- **IP Lookup**: Pulls geo and network info for any IP address using public APIs.
- **URL/Web Scanner**: Checks for common vulnerable endpoints and basic web vulns (SQLi/XSS).
- **Modular Design**: Each function in its own file, easy to extend or modify.
- **Menu-Driven Interface**: User-friendly CLI for beginners and pros.

## 📦 Installation

### 1. Clone the Repository

`git clone https://github.com/agent-502/Hescan.git`

`cd Hescan`


### 2. Install Dependencies

Make sure you have Python 3.x installed, then run:

`pip install -r requirements.txt`


> **Note:**  
> - If you face issues installing `python-nmap`, ensure you have Nmap installed on your system (see below).  
> - On some systems, use `python3` and `pip3` instead of `python` and `pip`.

### 3. Install Nmap Executable

The Python package `python-nmap` is only a wrapper; you need to install the Nmap tool itself:

- **Linux (Debian/Ubuntu):**

`sudo apt install nmap`


- **macOS (with Homebrew):**

`brew install nmap`


- **Windows:**

```Download and install from``` [https://nmap.org/download.html](https://nmap.org/download.html).

## 🚀 Usage

### Running HeScan

From the **CMD**:

`python -m hescan`


Or just run the script (*run.py*):

`python run.py`


### Available Options in the Menu

1. **LAN Network Scan** — Discover live hosts on the LAN via ARP scanning.  
2. **WiFi Scanner** — List visible WiFi networks (platform-dependent).  
3. **Port Scanner** — Scan open TCP ports on an IP/host with a customizable range.  
4. **Vulnerability Scan** — Perform deep service/version detection and vulnerability checks via Nmap.  
5. **IP Lookup** — Get geolocation and organization info about an IP address.  
6. **URL Scan** — Scan website endpoints for common vulnerabilities and exposures (e.g., admin pages, .git, SQLi/XSS checks).  
7. **Exit** — Quit the program.

## 🌐 Supported Platforms

- **Linux:** Full feature support.  
- **macOS:** Most features available; WiFi scanning uses system-specific tools.  
- **Windows:** Supported; WiFi scanning uses `netsh`; requires Nmap installed.

> **Administrator/root privileges are required** for some network, WiFi scanning, and port scanning features.

## ⚠️ Legal Notice

HeScan is for **educational and authorized security testing only**.  
Do not scan or probe any network or system without explicit permission.  
Unauthorized scanning is illegal and unethical.

## 💡 Credits & Inspiration

- Inspired by frameworks and tools such as Metasploit, Nmap, Scapy.  
- Uses Python libraries:  
  - [scapy](https://github.com/secdev/scapy)  
  - [python-nmap](https://xael.org/pages/python-nmap-en.html)  
  - [requests](https://docs.python-requests.org/en/latest/)

**Created by:** agent-502
**Year:** 2025

## 🌟 Contributing

Contributions, pull requests, and new feature ideas are welcome! Please respect legal and ethical standards when developing and using security tools.

## 📄 License

Released under the MIT License — see the [`License`](https://github.com/uustuff/Hescan/blob/main/LICENSE) file for details.

---

**Happy hacking (responsibly) with HeScan!** 🚀
