import time
import psycopg2
from DML.modify import Check_Author


def Delete_Author(address):

    wanted_author = input("Digite o nome do autor que deseja excluir: ")

    try:
        conn = psycopg2.connect(
            database=address[0],
            user=address[1],
            password=address[2],
            host=address[3],
            port=address[4]
        )

        # Criar um cursor para executar as consultas
        cursor = conn.cursor()

        query = "DELETE FROM livros WHERE autor = %s"
        cursor.execute(query, (wanted_author,))

        query = "DELETE FROM autores WHERE autor = %s"
        cursor.execute(query, (wanted_author,))

        conn.commit()



        # rowcount retorna o número de linhas afetadas pelo comando SQL
        if cursor.rowcount > 1:
            print(f"{cursor.rowcount} livros excluídos com sucesso, além do autor.")
        else:
            print(f"{cursor.rowcount} livro excluído com sucesso, além do autor.")

    except psycopg2.Error as error:
        print("\n\nOcorreu um erro ao conectar ou manipular o banco de dados:", error)
        time.sleep(2)
    finally:
        if cursor is not None:
            cursor.close()

        if conn is not None:
            conn.close()




def Delete_Book(address):
    wanted_book_id = input("Digite o ID do livro que deseja excluir: ")

    try:
        conn = psycopg2.connect(
            database=address[0],
            user=address[1],
            password=address[2],
            host=address[3],
            port=address[4]
        )

        # Criar um cursor para executar as consultas
        cursor = conn.cursor()

        query = "DELETE FROM livros WHERE id = %s"
        cursor.execute(query, (wanted_book_id,))
        conn.commit()

        # rowcount retorna o número de linhas afetadas pelo comando SQL
        if cursor.rowcount == 1:
            print("Livro excluído com sucesso.")
        else:
            print("Nenhum livro encontrado com o ID fornecido.")

    except psycopg2.Error as error:
        print("\n\nOcorreu um erro ao conectar ou manipular o banco de dados:", error)
        time.sleep(2)
    finally:
        if cursor is not None:
            cursor.close()

        if conn is not None:
            conn.close()