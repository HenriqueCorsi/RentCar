import mysql.connector

def sql_connector(table):
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='123456',
        database='rentcar'
    )

    cursor = connection.cursor()

    command = f'SELECT * FROM {table}'

    cursor.execute(command)

    # Obter os nomes das colunas
    column_names = [desc[0] for desc in cursor.description]

    # Imprimir cabeçalhos
    print(' | '.join(column_names))
    print('-' * 100)  # Linha de separação

    # Imprimir os dados
    for row in cursor.fetchall():
        # Formatando cada linha de dados
        formatted_row = ' | '.join(str(value) for value in row)
        print(formatted_row)

    # Fechar cursor e conexão
    cursor.close()
    connection.close()


