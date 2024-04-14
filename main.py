from features import menu
from time import sleep
from os import system
from features.customer_registration import *
from features.mysql_connector import sql_connector

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
            first_name = get_first_name()
            last_name = get_last_name()
            email = get_email()
            phone = get_phone_number()
            date = get_date()
            licence_number = get_licence_number()
            date_day = get_registration_date()
            status = 1
            
            table = 'cliente'
            column_customer = ('primeiro_nome', 'ultimo_nome', 'email', 'telefone', 'data_nascimento', 'num_habilitacao', 'data_registro', 'status_ativacao') 
            formatted_column = ', '.join(column_customer)
            values = (first_name, last_name, email, phone, date, licence_number, date_day, status)

            sql_connector(table, formatted_column, values)
        
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