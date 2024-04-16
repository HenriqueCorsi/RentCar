#reservation registration
from customer_registration import exit_except
from os import system
from time import sleep
import re

#Pega Data Inicio
def get_start_date():
    date_pattern = re.compile(r"^\d{4}-\d{2}-\d{2}$")

    while True:
        try:
            system('cls')
            start_date = input('Data Ínicio (ANO-MÊS-DIA): ')
            sleep(1)
            if date_pattern.match(start_date ):
                return start_date 
            else:
                exit_except()
        except Exception as e:
            exit_except()

#Pega Data Termino
def get_end_date():
    date_pattern = re.compile(r"^\d{4}-\d{2}-\d{2}$")

    while True:
        try:
            system('cls')
            end_date = input('Data Termino (ANO-MÊS-DIA): ')
            sleep(1)
            if date_pattern.match(end_date ):
                return end_date 
            else:
                exit_except()
        except Exception as e:
            exit_except()

