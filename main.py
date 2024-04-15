from menu import *
from time import sleep
from os import system
from customer_registration import *
from veiculo_cadastro import *
from mysql_connector import sql_connector

while True:
    home_menu()
    options_menu()
    try:
        select_user = int(input(''))
    except Exception as e:
        system('cls')
        print('Valor Inválido!!')
        sleep(1)
        system('cls')
    else:
        if select_user == 1: # Cadastro de Cliente
            try:
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
            except Exception as e:
                print(f'Erro: {e}')
            else:
                system('cls')
                print('Carregando...')
                sleep(1)
                system('cls')
                print('Cadastro Realizado com Sucesso!!')
                sleep(1)
            
            break
        elif select_user == 2: # Cadastro de Veículo
            try:
                brand = get_brand()
                model = get_model()
                vehicle_year = get_year()
                plate = get_plate()
                vehicle_color = get_color()
                type_fuel = get_type_fuel()
                availability = get_availabe()
                daily_price = get_daily_value()

                table = 'veiculo'
                column_vehicle = ('marca', 'modelo', 'ano', 'placa', 'cor', 'tipo_combustivel', 'disponivel', 'valor_diaria')
                formatted_column = ', '.join(column_vehicle )
                values = (brand, model, vehicle_year, plate, vehicle_color, type_fuel, availability, daily_price)

                sql_connector(table, formatted_column, values)
            except Exception as e:
                print(f'Erro: {e}')
            else:
                system('cls')
                print('Carregando...')
                sleep(1)
                system('cls')
                print('Cadastro Realizado com Sucesso!!')
                sleep(1)
            
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