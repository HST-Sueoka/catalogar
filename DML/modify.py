import time
import psycopg2
from support.normalize import normalizar_palavra



def Check_Author(wanted_author, address):
    print("\nVerificando a existência do autor.\n")

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

        # Obtém os autores existentes no banco de dados
        query = "SELECT autor FROM autores"
        cursor.execute(query)
        existing_author = cursor.fetchall()

        existing_author_normalized = [normalizar_palavra(author[0]) for author in existing_author]

        normalized_wanted = normalizar_palavra(wanted_author)

        if normalized_wanted in existing_author_normalized:
            index = existing_author_normalized.index(normalized_wanted)
            wanted_author = existing_author[index][0]
            flag_author = False
        else:
            flag_author = True

    except Exception as error:
        print("\n\nOcorreu um erro ao conectar ou manipular o banco de dados:", error)
        time.sleep(3)

    finally:
        if cursor is not None:
            cursor.close()

        if conn is not None:
            conn.close()

    return wanted_author, flag_author



def Check_Book(wanted_author, wanted_title, wanted_language, address):
    print("\nVerificando a existência do livro.\n")

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

        # Obtém os livros existentes no banco de dados
        query = "SELECT autor, titulo, idioma FROM livros Where autor = %s"
        cursor.execute(query, (wanted_author,))
        existing_books = cursor.fetchall()

        existing_books_normalized = [(normalizar_palavra(book[0]), normalizar_palavra(book[1]), normalizar_palavra(book[2])) for book in existing_books]

        normalized_wanted_author = normalizar_palavra(wanted_author)
        normalized_wanted_title = normalizar_palavra(wanted_title)
        normalized_wanted_language = normalizar_palavra(wanted_language)

        if (normalized_wanted_author, normalized_wanted_title, normalized_wanted_language) in existing_books_normalized:
            index = existing_books_normalized.index((normalized_wanted_author, normalized_wanted_title, normalized_wanted_language))
            wanted_author = existing_books[index][0]
            wanted_title = existing_books[index][1]
            wanted_language = existing_books[index][2]
            flag_book = False
        else:
            flag_book = True
            

    except Exception as error:
        print("\n\nOcorreu um erro ao conectar ou manipular o banco de dados:", error)
        time.sleep(3)

    finally:
        if cursor is not None:
            cursor.close()

        if conn is not None:
            conn.close()

    return wanted_author, wanted_title, wanted_language, flag_book