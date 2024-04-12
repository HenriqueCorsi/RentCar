from time import sleep
from os import system
import re

def exit_except():
    system('cls')
    print("Valor Inválido")
    sleep(1)
    system('cls')

#Pega Primeiro Nome
def get_first_name():
    while True:
        try:
            system('cls')
            first_name = input("Primeiro Nome: ").strip() 
            if first_name:
                return first_name
            else:
                exit_except()
                
        except Exception as e:
            exit_except()

#Pega Ultimo Nome
def get_last_name():
    while True:
        try:
            system('cls')
            last_name = input("Último Nome: ").strip() 
            if last_name:
                return last_name
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

            if date_pattern.match(date):
                return date
            else:
                exit_except()
        except Exception as e:
            exit_except()

def get_licence_number():
    while True:
        try:
            system('cls')
            licence_number = int(input('Número Habilitação: '))  
        except Exception as e:
            exit_except()
        else:
            licence_number = str(licence_number)
            if len(licence_number) == 12:
                return licence_number
            else:
                exit_except()
        
