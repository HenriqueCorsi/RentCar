from menu import *
from time import sleep
from os import system
from customer_registration import *
from veiculo_cadastro import *
from mysql_connector import sql_connector
from view import sql_connector_view

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
        # Cadastro de Cliente
        if select_user == 1: 
            try:
                cpf = get_cpf()
                first_name = get_first_name()
                surname = get_surname()
                email = get_email()
                phone = get_phone_number()
                date = get_date()
                licence_number = get_licence_number()
                date_day = get_registration_date()
                
                table = 'cliente'
                column_customer = ('cpf', 'primeiro_nome', 'sobrenome', 'email', 'telefone', 'data_nascimento', 'num_habilitacao', 'data_registro') 
                formatted_column = ', '.join(column_customer)
                values = (cpf, first_name, surname, email, phone, date, licence_number, date_day)
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

        # Cadastro de Veículo
        elif select_user == 2: 
            try:
                plate = get_plate()
                brand = get_brand()
                model = get_model()
                vehicle_year = get_year()
                category = get_category()
                vehicle_color = get_color()
                type_fuel = get_type_fuel()
                availability = get_availabe()
                daily_price = get_daily_value()

                table = 'veiculo'
                column_vehicle = ('placa', 'marca', 'modelo', 'ano', 'categoria', 'cor', 'tipo_combustivel', 'disponivel', 'valor_diaria')
                formatted_column = ', '.join(column_vehicle )
                values = (plate, brand, model, vehicle_year, category, vehicle_color, type_fuel, availability, daily_price)
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

        #Cadastrar Reserva
        elif select_user == 3:
            pass

        # Vizualizar todos os Clientes Cadastrados
        elif select_user == 4:  
            table = 'cliente'
            system('cls')
            sql_connector_view(table)
            break

        # Vizualizar todos os veículs Cadastrados
        elif select_user == 5: 
            table = 'veiculo'
            system('cls')
            sql_connector_view(table)
            break

        # Vizualizar Reservas Cadastradas
        elif select_user == 6: 
            pass

        # Sair
        elif select_user == 7: 
            system('cls')
            print('Até Breve!!')
            sleep(1)
            system('cls')
            break
        
        # Valores fora do Range
        else: 
           system('cls')
           print('Valor Inválido!!')
           sleep(1)
           system('cls')