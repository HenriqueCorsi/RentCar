# vehicle registration
from customer_registration import exit_except

#Pega Marca
def get_brand():
    while True:
        try:
            brand = input('Marca: ')
        except Exception as e:
            exit_except()
        else:
            if brand:
                return brand
            else:
                exit_except()        

#Pega Modelo
def get_model():
    pass

#Pega Ano
def get_year():
    pass

#Pega Placa
def get_plate():
    pass

#Pega Cor
def get_color():
    pass

#Pega Tipo de Combustivel
def get_type_fuel():
    pass

#Pega Disponibilidade
def get_availabe():
    pass

#Pega Valor Diaria
def get_daily_value():
    pass
