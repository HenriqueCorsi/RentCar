from features import menu
from time import sleep
from os import system

while True:
    menu.home_menu()
    menu.options_menu()
    try:
        select_user = int(input(''))
    except Exception as e:
        system('cls')
        print('Valor Inválido!!')
        sleep(1)
        system('cls')
    else:
        if select_user == 1: # Cadastro de Cliente
            pass
            break
        elif select_user == 2: # Cadastro de Veículo
            pass
            break
        elif select_user == 3: # Cadastro de Reserva
            pass
            break
        elif select_user == 4: # Cadastro de Transação
            pass
            break
        elif select_user == 5: # Sair
            pass
            break
        else: # Valores fora do Range
           system('cls')
           print('Valor Inválido!!')
           sleep(1)
           system('cls')