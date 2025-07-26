import subprocess
import platform

def scan_wifi():
    print("[+] Scanning for WiFi networks...")
    system = platform.system()
    try:
        if system == "Windows":
            result = subprocess.check_output(['netsh', 'wlan', 'show', 'network'])
            print(result.decode("utf-8", errors="ignore"))
        elif system == "Linux":
            result = subprocess.check_output(['nmcli', '-f', 'SSID,SECURITY,SIGNAL', 'device', 'wifi', 'list'])
            print(result.decode())
        elif system == "Darwin":  # macOS
            result = subprocess.check_output(['/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport', '-s'])
            print(result.decode())
        else:
            print("WiFi scanning not supported on this OS.")
    except Exception as e:
        print(f"Error: {e}")
