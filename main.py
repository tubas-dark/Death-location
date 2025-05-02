import socket
import requests
import ipaddress
import os

API_KEY = "24ef3502fbc459745f77b866f6bcd5fe"

# Cores ANSI
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
RESET = '\033[0m'

def limpar_tela():
    os.system("clear")

def exibir_menu():
    print(f"{BLUE}╔══════════════════════════════╗{RESET}")
    print(f"{BLUE}║     Scriptv2 By Dark         ║{RESET}")
    print(f"{BLUE}╠══════════════════════════════╣{RESET}")
    print(f"{RED}[1] Localizar número{RESET}")
    print(f"{RED}[2] Localizar IP{RESET}")
    print(f"{RED}[3] IP Location {RESET}")
    print(f"{RED}[0] Sair{RESET}")
    print(f"{BLUE}╚══════════════════════════════╝{RESET}")

def localizar_numero():
    numero = input("Digite o número com código do país (ex: +5511999999999): ")
    url = f"http://apilayer.net/api/validate?access_key={API_KEY}&number={numero}&country_code=&format=1"
    resposta = requests.get(url).json()

    print("📞 Resultado da Localização:")
    print(f"Número: {resposta.get('international_format')}")
    print(f"País: {resposta.get('country_name')}")
    print(f"Localização: {resposta.get('location')}")
    print(f"Operadora: {resposta.get('carrier')}")
    print(f"Linha Fixa?: {resposta.get('line_type')}")
    input("\nPressione Enter para continuar...")

def localizar_ip():
    ip = input("Digite o IP para localizar: ")
    resposta = requests.get(f"http://ip-api.com/json/{ip}").json()

    if resposta.get("status") == "success":
        print("🌐 Resultado da Localização IP:")
        print(f"IP: {resposta.get('query')}")
        print(f"País: {resposta.get('country')}")
        print(f"Região: {resposta.get('regionName')}")
        print(f"Cidade: {resposta.get('city')}")
        print(f"Provedor: {resposta.get('isp')}")
        print(f"Org: {resposta.get('org')}")
        print(f"Lat/Lon: {resposta.get('lat')}, {resposta.get('lon')}")
    else:
        print("❌ Não foi possível localizar o IP.")
        print(f"Motivo: {resposta.get('message', 'Erro desconhecido')}")

    input("\nPressione Enter para continuar...")

def localizar_ip_completo():
    ip = input(f"\n{CYAN}Digite o IP para localizar (pressione enter): {RESET}").strip()

    if ip == "":
        try:
            resposta_publica = requests.get("http://ip-api.com/json/").json()

            if resposta_publica["status"] == "success":
                print(f"\n{GREEN}🌍 LOCALIZAÇÃO DO SEU IP PÚBLICO:{RESET}")
                print(f"🔹 IP: {resposta_publica.get('query', 'N/A')}")
                print(f"🌎 País: {resposta_publica.get('country', 'N/A')}")
                print(f"🏙️ Cidade: {resposta_publica.get('city', 'N/A')}")
                print(f"🌐 Região: {resposta_publica.get('regionName', 'N/A')}")
                print(f"🛰️ ISP: {resposta_publica.get('isp', 'N/A')}")
                print(f"📍 Lat/Lon: {resposta_publica.get('lat')} / {resposta_publica.get('lon')}")

            ip_local = socket.gethostbyname(socket.gethostname())
            print(f"\n{BLUE}🔒 Seu IP local (privado): {ip_local}{RESET}")

        except Exception as e:
            print(f"{RED}❌ Erro ao obter IP público/local: {e}{RESET}")
        return

    try:
        ip_obj = ipaddress.ip_address(ip)
        if ip_obj.is_private:
            print(f"{RED}❌ IP está em faixa privada, não é possível obter localização pública.{RESET}")
            return

        resposta = requests.get(f"http://ip-api.com/json/{ip}").json()
        if resposta["status"] == "success":
            print(f"\n{GREEN}📡 LOCALIZAÇÃO DO IP {ip}:{RESET}")
            print(f"🌍 País: {resposta.get('country', 'N/A')}")
            print(f"🏙️ Cidade: {resposta.get('city', 'N/A')}")
            print(f"🌐 Região: {resposta.get('regionName', 'N/A')}")
            print(f"🛰️ ISP: {resposta.get('isp', 'N/A')}")
            print(f"📍 Lat/Lon: {resposta.get('lat')} / {resposta.get('lon')}")
        else:
            print(f"{RED}❌ Não foi possível localizar o IP.{RESET}")
            print(f"Motivo: {resposta.get('message', 'Desconhecido')}")
    except ValueError:
        print(f"{RED}❌ IP inválido!{RESET}")

def main():
    while True:
        limpar_tela()
        exibir_menu()

        escolha = input(f"\n{CYAN}Escolha uma opção:{RESET} ").strip()

        if escolha == "1":
            print(f"\n{RED}🔍 OPÇÃO 1: LOCALIZAR NÚMERO{RESET}")
            localizar_numero()
        elif escolha == "2":
            print(f"\n{RED}🌐 OPÇÃO 2: LOCALIZAR IP{RESET}")
            localizar_ip()
        elif escolha == "3":
            print(f"\n{RED}📡 OPÇÃO 3: IP LOCATION COMPLETA{RESET}")
            localizar_ip_completo()
        elif escolha == "0":
            print(f"\n{RED}Saindo...{RESET}")
            break
        else:
            print(f"\n{RED}❌ Opção inválida.{RESET}")

        input(f"\n{BLUE}Pressione Enter para continuar...{RESET}")

if __name__ == "__main__":
    main()

