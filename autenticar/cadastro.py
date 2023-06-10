from ast import main
import psycopg2


def cadastrar_usuario(nome, email, senha, address):
    flag = False
    try:
        connection = psycopg2.connect(
            database=address[0],
            user=address[1],
            password=address[2],
            host=address[3],
            port=address[4]
        )

        cursor = connection.cursor()

        # Seleciona o usuário pelo email
        cursor.execute('SELECT * FROM usuarios WHERE email = %s', (email,))
        resultado = cursor.fetchone()

        if resultado is None:
            query = "INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)"
            cursor.execute(query, (nome, email, senha))
            connection.commit()
            flag = True

        else:
            # O usuário não foi encontrado
            print("\nE-mail já cadastrado.")


    except Exception as error:
        print("\nOcorreu um erro ao conectar ou manipular o banco de dados:", error)
        if __name__ == "__main__":
            main()
            
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()
        if __name__ == "__main__":
            main()
