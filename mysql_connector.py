import mysql.connector

def sql_connector(table, column, value, markers):
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='123456',
        database='rentcar'
    )

    cursor = connection.cursor()

    command = f'''
                INSERT INTO {table}
                    ({column})
                VALUES
                    {markers}
'''

    cursor.execute(command, value) #Execua o comando SQL

    connection.commit() #Faz o commit pra dentro do Banco de Dados

    cursor.close() #Fecha conexão
    connection.close() #Fecha conexão




