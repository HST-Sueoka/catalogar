import time
import psycopg2
from DML.modify import Check_Author


def Update_Author(address):
    wanted_remove_author = input("Digite o nome do autor que deseja atualizar: ")
    wanted_update_author = input("Digite o nome do autor que deseja inserir: ")

    try:
        conn = psycopg2.connect(
            database=address[0],
            user=address[1],
            password=address[2],
            host=address[3],
            port=address[4]
        )





def Update_Book(address):
    wanted_book_id = input("Digite o ID do livro que deseja atualizar: ")

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


    except psycopg2.Error as error:
        print("\n\nOcorreu um erro ao conectar ou manipular o banco de dados:", error)
        time.sleep(2)
    finally:
        if cursor is not None:
            cursor.close()

        if conn is not None:
            conn.close()
