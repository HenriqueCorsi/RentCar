import mysql.connector
from customer_registration import *

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
                    (primeiro_nome, ultimo_nome, email, telefone, data_nascimento, num_habilitacao, data_registro, status_ativacao)  
                VALUES
                    (%s, %s, %s, %s, %s, %s, %s, %s)
'''

    cursor.execute(command) #Execua o comando SQL

    connection.commit() #Faz o commit pra dentro do Banco de Dados

    cursor.close() #Fecha conexão
    connection.close() #Fecha conexão





