import os
import subprocess
import sys



def install_requirements():
    required_packages = {
        'requests': 'requests',
        'colorama': 'colorama',
        'ipaddress': 'ipaddress',
        'pyfiglet': 'pyfiglet',
        'ssl': 'ssl',
        'beautifulsoup4': 'bs4',
        'dnspython': 'dns',
        'multithreading': 'multithreading',
        'loguru': 'loguru'
    }

    for package, import_name in required_packages.items():
        try:
            __import__(import_name)
        except ImportError:
            print(f"\033[33m⏳ Instalando '{package}'...\033[0m")
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"\033[32m✅ '{package}' instalado.\033[0m")

install_requirements()

from colorama import Fore, Style, Back, init
import pyfiglet

init(autoreset=True)



def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')



def text_to_ascii_banner(text, font="doom", color=Fore.WHITE):
    try:
        ascii_banner = pyfiglet.figlet_format(text, font=font)
        colored_banner = f"{color}{ascii_banner}{Style.RESET_ALL}"
        return colored_banner
    except pyfiglet.FontNotFound:
        return "Font not found."



def get_input(prompt, default=None):
    response = input(prompt + Style.BRIGHT).strip()
    print(Style.RESET_ALL)
    return response if response else default or ""



def banner():
    clear_screen()
    print(text_to_ascii_banner("BugScanX", font="doom", color=Style.BRIGHT + Fore.CYAN))
    print(Fore.CYAN + "  🔧 Fork por: " + Fore.LIGHTCYAN_EX + Style.BRIGHT + "Aurelhopedro (Aurélio Machai)")
    print(Fore.BLUE + " 🌍 Benguela, Angola")
    print(Fore.WHITE + Style.DIM + "\nFerramenta para encontrar SNI bug hosts\n")
    print(Style.RESET_ALL)



def main_menu():
    while True:
        banner()
        print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "Seleciona uma opção:" + Style.RESET_ALL)
        print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\n [1] ⚡  Host Scanner")
        print(Fore.LIGHTYELLOW_EX + " [2] 🖥️   Scanner de Subdomínios")
        print(Fore.LIGHTYELLOW_EX + " [3] 📡  Scanner de IPs")
        print(Fore.LIGHTYELLOW_EX + " [4] 🌐  Encontrar Subdomínios")
        print(Fore.LIGHTYELLOW_EX + " [5] 🔍  Domínios no mesmo IP")
        print(Fore.LIGHTYELLOW_EX + " [6] ✂️   TXT Toolkit")
        print(Fore.LIGHTYELLOW_EX + " [7] 🔓  Verificar Portas Abertas")
        print(Fore.LIGHTYELLOW_EX + " [8] 📜  Registos DNS")
        print(Fore.LIGHTYELLOW_EX + " [9] 🔬  OSINT do Host")
        print(Fore.LIGHTYELLOW_EX + " [10] 📖  Ajuda")
        print(Fore.LIGHTRED_EX + Style.BRIGHT + " [0]  ⛔  Sair\n" + Style.RESET_ALL)

        choice = get_input(Fore.CYAN + " ➜  Escolha (0-10): ").strip()

        if choice == '1':
            clear_screen()
            print(text_to_ascii_banner("HOST Scanner", font="doom", color=Style.BRIGHT + Fore.CYAN))
            import modules.host_scanner as host_scanner
            host_scanner.bugscanner_main()
            input(Fore.YELLOW + "\n Prima Enter para voltar ao menu...")

        elif choice == "2":
            clear_screen()
            print(text_to_ascii_banner("Sub Scanner", font="doom", color=Style.BRIGHT + Fore.CYAN))
            import modules.sub_scan as sub_scan
            hosts, ports, output_file, threads, method = sub_scan.get1_scan_inputs()
            if hosts is None:
                continue
            sub_scan.perform1_scan(hosts, ports, output_file, threads, method)
            input(Fore.YELLOW + "\n Prima Enter para voltar ao menu...")

        elif choice == "3":
            clear_screen()
            print(text_to_ascii_banner("IP Scanner", font="doom", color=Style.BRIGHT + Fore.CYAN))
            import modules.ip_scan as ip_scan
            hosts, ports, output_file, threads, method = ip_scan.get2_scan_inputs()
            if hosts is None:
                continue
            ip_scan.perform2_scan(hosts, ports, output_file, threads, method)
            input(Fore.YELLOW + "\n Prima Enter para voltar ao menu...")

        elif choice == "4":
            clear_screen()
            print(text_to_ascii_banner("Subfinder", font="doom", color=Style.BRIGHT + Fore.CYAN))
            import modules.sub_finder as sub_finder
            sub_finder.find_subdomains()
            input(Fore.YELLOW + "\n Prima Enter para voltar ao menu...")

        elif choice == "5":
            clear_screen()
            print(text_to_ascii_banner("IP LookUp", font="doom", color=Style.BRIGHT + Fore.CYAN))
            import modules.ip_lookup as ip_lookup
            ip_lookup.Ip_lockup_menu()
            input(Fore.YELLOW + "\n Prima Enter para voltar ao menu...")

        elif choice == "6":
            clear_screen()
            print(text_to_ascii_banner("TXT Toolkit", font="doom", color=Style.BRIGHT + Fore.CYAN))
            import modules.txt_toolkit as txt_toolkit
            txt_toolkit.txt_toolkit_main_menu()
            input(Fore.YELLOW + "\n Prima Enter para voltar ao menu...")

        elif choice == "7":
            clear_screen()
            print(text_to_ascii_banner("Open Port", font="doom", color=Style.BRIGHT + Fore.CYAN))
            import modules.open_port as open_port
            open_port.open_port_checker()
            input(Fore.YELLOW + "\n Prima Enter para voltar ao menu...")

        elif choice == "8":
            clear_screen()
            print(text_to_ascii_banner("DNS Records", font="doom", color=Style.BRIGHT + Fore.CYAN))
            domain = get_input(Fore.CYAN + " ➜  Insere o domínio para NSLOOKUP: ").strip()
            import modules.dns_info as dns_info
            dns_info.nslookup(domain)
            input(Fore.YELLOW + "\n Prima Enter para voltar ao menu...")

        elif choice == "9":
            clear_screen()
            print(text_to_ascii_banner("OSINT", font="doom", color=Style.BRIGHT + Fore.CYAN))
            import modules.osint as osint
            osint.osint_main()
            input(Fore.YELLOW + "\n Prima Enter para voltar ao menu...")

        elif choice == "10":
            clear_screen()
            import modules.script_help as script_help
            script_help.show_help()
            input(Fore.YELLOW + "\n Prima Enter para voltar ao menu...")

        elif choice == "0":
            print(Fore.RED + Style.BRIGHT + "\n🔴 A fechar. Até logo!")
            sys.exit()

        else:
            print(Fore.RED + Style.BRIGHT + "\n⚠️ Opção inválida.")
            input(Fore.YELLOW + Style.BRIGHT + "\n Prima Enter para continuar...")



if __name__ == "__main__":
    main_menu()
