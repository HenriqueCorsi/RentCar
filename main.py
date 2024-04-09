from features import menu

menu.home_menu()
menu.options_menu()


while True:
    try:
        select_user = int(input(''))
    except Exception as e:
        print('Valor Inválido')
    else:
        if select_user == 1: # Cadastro de Cliente
            pass
        elif select_user == 2: # Cadastro de Veículo
            pass
        elif select_user == 3: # Cadastro de Reserva
            pass
        elif select_user == 4: # Cadastro de Transação
            pass
        elif select_user == 5: # Sair
            pass
        else:
            pass