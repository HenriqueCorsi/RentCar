import os

def home_menu():
    os.system('cls')
    print('================================')
    print('            RENTCAR             ')
    print('================================')

def options_menu():
    options = ['1 -> Cadastrar Cliente', '2 -> Cadastrar Veículo', '3 -> Vizualizar Clientes', '4 -> Vizualzar Veículos', '5 -> Sair']

    for x in options:
        print(x)