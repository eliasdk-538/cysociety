import os
import time
import random
import nmap
import requests

# Limpar terminal
def clear_terminal():
    os.system("clear")

# ASCII ART
ascii_art = r"""
▄▄·  ▄· ▄▌▄▄▄▄· ▄▄▄ .▄▄▄      .▄▄ ·        ▄▄· ▪  ▄▄▄ .▄▄▄▄▄ ▄· ▄▌
▐█ ▌▪▐█▪██▌▐█ ▀█▪▀▄.▀·▀▄ █·    ▐█ ▀. ▪     ▐█ ▌▪██ ▀▄.▀·•██  ▐█▪██▌
██ ▄▄▐█▌▐█▪▐█▀▀█▄▐▀▀▪▄▐▀▀▄     ▄▀▀▀█▄ ▄█▀▄ ██ ▄▄▐█·▐▀▀▪▄ ▐█.▪▐█▌▐█▪
▐███▌ ▐█▀·.██▄▪▐█▐█▄▄▌▐█•█▌    ▐█▄▪▐█▐█▌.▐▌▐███▌▐█▌▐█▄▄▌ ▐█▌· ▐█▀·.
·▀▀▀   ▀ • ·▀▀▀▀  ▀▀▀ .▀  ▀     ▀▀▀▀  ▀█▄▀▪·▀▀▀ ▀▀▀ ▀▀▀  ▀▀▀   ▀ • 
"""

# Progresso fake (apenas visual)
def progress_bar(task_name):
    for i in range(101):
        time.sleep(0.03)
        print(f"\r[{task_name} - CYBER SOCIETY = {i}%]", end="", flush=True)
    print()

# Scan real de portas com nmap
def scan_ports(host):
    nm = nmap.PortScanner()
    nm.scan(host, arguments="-Pn -T4 --top-ports 100")
    print("\nPORTAS ABERTAS ___________________")
    for proto in nm[host].all_protocols():
        ports = nm[host][proto].keys()
        for port in sorted(ports):
            state = nm[host][proto][port]['state']
            name = nm[host][proto][port]['name']
            status = "ON" if state == "open" else "OFF"
            print(f"{port} - {name.upper()} - {status}")

# Descoberta de diretórios ocultos
def scan_directories(url):
    wordlist = ["admin", "login", "dashboard", "config", "password", "backup", "cpanel", "private"]
    print("\nACESSOS _______________________")
    for path in wordlist:
        full_url = f"{url.rstrip('/')}/{path}"
        try:
            r = requests.get(full_url, timeout=3)
            if r.status_code < 400:
                print(full_url)
        except:
            pass
        time.sleep(0.1)

# Programa principal
def main():
    clear_terminal()
    print(ascii_art)

    url = input("URL: ").strip()
    host = url.replace("http://", "").replace("https://", "").split("/")[0]

    nmap_scan = input("NMAP SCANING [y/n]: ").lower()
    if nmap_scan == "y":
        scanning = input("SCANING [Y/N]: ").lower()
        if scanning == "y":
            progress_bar("SCANING")
            scan_ports(host)
            scan_directories(url)
        else:
            print("Scan cancelado.")
    else:
        print("NMAP Scan ignorado.")

if __name__ == "__main__":
    main()
