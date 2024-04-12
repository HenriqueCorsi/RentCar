import mysql.connector
from datetime import date
from time import sleep
from os import system

def get_first_name():
    while True:
        try:
            first_name = input("Primeiro Nome: ").strip() 
            if first_name:
                return first_name
            else:
                system('cls')
                print("Valor Inválido")
                sleep(1)
                system('cls')
                
        except Exception as e:
            system('cls')
            print("Valor Inválido")
            sleep(1)
            system('cls')


def get_last_name():
    while True:
        try:
            last_name = input("Último Nome: ").strip() 
            if last_name:
                return last_name
            else:
                system('cls')
                print("Valor Inválido")
                sleep(1)
                system('cls')
                
        except Exception as e:
            system('cls')
            print("Valor Inválido")
            sleep(1)
            system('cls')









def sql_connector():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='123456',
        database='rentcar'
    )

    cursor = connection.cursor()

    command = f'''
                INSERT INTO cliente 
                    (cliente_id, primeiro_nome, ultimo_nome, email, telefone, data_nascimento, num_habilitacao, data_registro, status_ativacao)  
                VALUES
                    (%s, %s, %s, %s, %s, %s, %s, %s, %s)
'''

    cursor.execute(command) #Execua o comando SQL

    connection.commit() #Faz o commit pra dentro do Banco de Dados

    cursor.close() #Fecha conexão
    connection.close() #Fecha conexão







