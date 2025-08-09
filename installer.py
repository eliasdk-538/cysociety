import os
import subprocess
import time

# Limpa o terminal
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

# Barra de progresso visual
def progress_bar(task_name):
    for i in range(101):
        time.sleep(0.02)
        print(f"\r[{task_name} - CYBER SOCIETY = {i}%]", end="", flush=True)
    print()

# Executa comando e mostra a saída em tempo real
def run_command(cmd):
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    for line in process.stdout:
        print(line, end="")
    process.wait()

# Instalação
def instalar():
    print("\n[+] Atualizando pacotes...\n")
    run_command("pkg update -y && pkg upgrade -y")
    print("\n[+] Instalando Python...\n")
    run_command("pkg install python -y")
    print("\n[+] Instalando Nmap...\n")
    run_command("pkg install nmap -y")
    print("\n[+] Instalando bibliotecas Python...\n")
    run_command("pip install python-nmap requests")

# Principal
def main():
    clear_terminal()
    print(ascii_art)
    print("\n=== INSTALADOR CYBER SOCIETY ===\n")
    start = input("Deseja instalar todos os pacotes necessários? [y/n]: ").lower()
    if start == "y":
        progress_bar("INICIANDO INSTALADOR")
        instalar()
        print("\n[✓] Instalação concluída!")
    else:
        print("Instalação cancelada.")

if __name__ == "__main__":
    main()
  
