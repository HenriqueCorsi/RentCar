import os

def home_menu():
    os.system('cls')
    print('================================')
    print('            RENTCAR             ')
    print('================================')

def options_menu():
    options = ['1 -> Cadastrar Cliente', '2 -> Cadastrar Veículo', '3 -> Cadastrar Reserva', '4 -> Vizualzar Clientes', '5 -> Vizualizar Veículos', '6 -> Vizualizar Reservas', '7 -> Sair']

    for x in options:
        print(x)
        print('--------------------------------')