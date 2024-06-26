from time import sleep
from os import system
import re
import datetime

def exit_except():
    system('cls')
    print("Valor Inválido")
    sleep(1)
    system('cls')

#Pega CPF
def get_cpf():
    cpf_pattern = re.compile(r'^\d{11}$')

    while True:
        try:
            system('cls')
            cpf = input('CPF: ').strip()
            sleep(1)
            if cpf and cpf_pattern.match(cpf):
                return cpf
            else:
                exit_except()
        except Exception as e:
            exit_except()

#Pega Primeiro Nome
def get_first_name():
    while True:
        try:
            system('cls')
            first_name = input("Primeiro Nome: ").strip() 
            sleep(1)
            if first_name:
                return first_name
            else:
                exit_except()
                
        except Exception as e:
            exit_except()

#Pega Sobrenome
def get_surname():
    while True:
        try:
            system('cls')
            surname = input("Último Nome: ").strip() 
            sleep(1)
            if surname:
                return surname
            else:
                exit_except()
                
        except Exception as e:
            exit_except()

#Pega Email
def get_email():
    email_pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')

    while True:
        try:
            system('cls')
            email = input("Email: ").strip() 
            sleep(1)
            if email and email_pattern.match(email):
                return email
            else:
                exit_except()
        except Exception as e:
            exit_except()
        
#Pega Telefone
def get_phone_number():
    number_pattern = re.compile(r"^\d{11}$")
    
    while True:
        try:
            system('cls')
            phone_number = input('Telefone: ').strip()  
            sleep(1)
            if number_pattern.match(phone_number):
                return phone_number
            else:
                exit_except()
        
        except Exception as e:
            exit_except()

#Pega Data
def get_date():
    date_pattern = re.compile(r"^\d{4}-\d{2}-\d{2}$")

    while True:
        try:
            system('cls')
            date = input('Data Nascimento (ANO-MÊS-DIA): ')
            sleep(1)
            if date_pattern.match(date):
                return date
            else:
                exit_except()
        except Exception as e:
            exit_except()

#Pega Númeor Habilitação
def get_licence_number():
    while True:
        try:
            system('cls')
            licence_number = int(input('Número Habilitação: '))  
            sleep(1)
        except Exception as e:
            exit_except()
        else:
            licence_number = str(licence_number)
            if len(licence_number) == 12:
                return licence_number
            else:
                exit_except()
        
#Registro automatico da data atual
def get_registration_date():
    registration_date = datetime.date.today()
    return registration_date

