from menu import *
from time import sleep
from os import system
from customer_registration import *
from veiculo_cadastro import *
from mysql_connector import sql_connector
from view_customer import sql_connector

while True:
    home_menu()
    options_menu()
    try:
        select_user = int(input('\n'))
    except Exception as e:
        system('cls')
        print('Valor Inválido!!')
        sleep(1)
        system('cls')
    else:
        if select_user == 1: # Cadastro de Cliente
            try:
                first_name = get_first_name()
                surname = get_surname()
                cpf = get_cpf()
                email = get_email()
                phone = get_phone_number()
                date = get_date()
                licence_number = get_licence_number()
                date_day = get_registration_date()
                
                table = 'cliente'
                column_customer = ('primeiro_nome', 'sobrenome', 'cpf', 'email', 'telefone', 'data_nascimento', 'num_habilitacao', 'data_registro') 
                formatted_column = ', '.join(column_customer)
                values = (first_name, surname, cpf, email, phone, date, licence_number, date_day)
                markers = f'(%s, %s, %s, %s, %s, %s, %s, %s)'

                sql_connector(table, formatted_column, values, markers)
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
                category = get_category()
                vehicle_color = get_color()
                type_fuel = get_type_fuel()
                availability = get_availabe()
                daily_price = get_daily_value()

                table = 'veiculo'
                column_vehicle = ('marca', 'modelo', 'ano', 'placa', 'categoria', 'cor', 'tipo_combustivel', 'disponivel', 'valor_diaria')
                formatted_column = ', '.join(column_vehicle )
                values = (brand, model, vehicle_year, plate, category, vehicle_color, type_fuel, availability, daily_price)
                markers = f'(%s, %s, %s, %s, %s, %s, %s, %s, %s)'

                sql_connector(table, formatted_column, values, markers)
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
        elif select_user == 3: # Vizualizar todos os Clientes Cadastrados
            table = 'cliente'
            system('cls')
            sql_connector(table)
            break
        elif select_user == 4: # Vizualizar todos os veículs Cadastrados
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