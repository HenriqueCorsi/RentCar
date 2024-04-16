# vehicle registration
from customer_registration import exit_except
from os import system
from time import sleep

#Pega Marca
def get_brand():
    while True:
        system('cls')
        try:
            brand = input('Marca: ')
            sleep(1)
        except Exception as e:
            exit_except()
        else:
            if brand:
                return brand
            else:
                exit_except()        

#Pega Modelo
def get_model():
      while True:
        system('cls')
        try:
            model = input('Modelo: ')
            sleep(1)
        except Exception as e:
            exit_except()
        else:
            if model:
                return model
            else:
                exit_except()        

#Pega Ano
def get_year():
    while True:
        system('cls')
        try:
            year = int(input('Ano: '))
            sleep(1)
        except Exception as e:
            exit_except()
        else:
            return year
        
#Pega Placa
def get_plate():
    while True:
        system('cls')
        try:
            plate = input('Placa: ')
            sleep(1)
        except Exception as e:
            exit_except()
        else:
            if len(plate) == 7:
                return plate
            else:
                exit_except() 

#Pega Categoria
def get_category():
    while True:
        system('cls')
        try:
            category = input('Categoria: ').lower()
            sleep(1)
        except Exception as e:
            exit_except()
        else:
            if category == 'hatch' or category == 'sedan' or category == 'suv':
                return category
            else:
                exit_except()
        
#Pega Cor
def get_color():
   while True:
        system('cls')
        try:
            color = input('Cor: ')
            sleep(1)
        except Exception as e:
            exit_except()
        else:
            if color:
                return color
            else:
                exit_except() 

#Pega Tipo de Combustivel
def get_type_fuel():
    while True:
        system('cls')
        try:
            type_fuel = input('Tipo Combustível: ').lower()
            sleep(1)
        except Exception as e:
            exit_except()
        else:
            if type_fuel == 'flex' or type_fuel == 'gasolina' or type_fuel == 'álcool':
                return type_fuel
            else:
                exit_except()

#Pega Disponibilidade
def get_availabe():
     while True:
        system('cls')
        try:
            availabe = input('Disponibilidade [S/N]: ').upper()
            sleep(1)
        except Exception as e:
            exit_except()
        else:
            if  availabe == 'S' or  availabe == 'N':
                return availabe
            else:
                exit_except()

#Pega Valor Diaria
def get_daily_value():
   while True:
        system('cls')
        try:
            daily_value = float(input('Valor Diária: R$'))
            sleep(1)
        except Exception as e:
            exit_except()
        else:
            return daily_value
