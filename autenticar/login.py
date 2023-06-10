import psycopg2

from support.menu import menu

def realizar_login(email, senha, address):
    id_usuario = 0

    try:
        connection = psycopg2.connect(
            database=address[0],
            user=address[1],
            password=address[2],
            host=address[3],
            port=address[4]
        )

        cursor = connection.cursor()

        # Verifica se o usuário existe na tabela e se a senha está correta
        cursor.execute('SELECT * FROM usuarios WHERE email = %s AND senha = %s', (email, senha))
        resultado = cursor.fetchone()

        if resultado is not None:
            print("Autentificação realizada com sucesso.")
            flag = True
            id_usuario = resultado[0]

        else:
            print("Autentificação inválida.")
            flag = False

    except Exception as error:
        print("\nOcorreu um erro ao conectar ou manipular o banco de dados:", error)

    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()
        if flag == True:
            menu(address, id_usuario)
    
    return flag, resultado[0]