from colorama import Fore, Style, init
init()

reservatorio = [100, 250, 500, 750, 1000]

def verificar_nivel(valor):
    if valor <= 100:
        print(Fore.RED + f"ALERTA CRÍTICO! Nível do reservatório muito abaixo do esperado: {valor} litros.")
        print(Style.RESET_ALL)
    
    elif valor <=250:
        print(Fore.YELLOW + f"Atenção! Nível do reservatório abaixo do esperado: {valor} litros.")
        print(Style.RESET_ALL)
    
    elif valor <=500:
        print(Fore.GREEN + f"Nível do reservatório estável {valor} litros.")
        print(Style.RESET_ALL)
    
    elif valor <=750:
        print(Fore.CYAN + f"Nível do reservatório alto {valor} litros.")
        print(Style.RESET_ALL)
    
    else:
        print(Fore.BLUE + f"Reservatório com capacidade elevada {valor} litros")
        print(Style.RESET_ALL)

for nivel in reservatorio:
    verificar_nivel(nivel)