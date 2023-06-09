
import time
import psycopg2
from DML.modify import Check_Author, Check_Book


def adicionar_autor(address):

    wanted_author = input("Digite o autor desejado: ")
    wanted_author, flag_author = Check_Author(wanted_author, address)

    if flag_author == True:
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

            query = "INSERT INTO autores (autor) VALUES (%s)"
            cursor.execute(query, (wanted_author,))
            conn.commit()

            print("\nAutor inserido com sucesso.\n")
            time.sleep(3)

        except psycopg2.Error as error:
            print("\nOcorreu um erro ao conectar ou manipular o banco de dados:", error)
            time.sleep(2)

        finally:
            if cursor is not None:
                cursor.close()

            if conn is not None:
                conn.close()
    else:
        print("Autor existente.")
        time.sleep(2)



def adicionar_livro(address):

    wanted_book = [
        input("Digite o autor do livro: "),
        input("Digite o título do livro: ")
    ]

    idioma_livro = input("Digite o idioma do livro (exemplos - pt, en, es, ru, fr): ")

    idiomas_permitidos = [
        'pt', 'en', 'es', 'fr', 'de', 'it', 'nl', 'ru', 'zh',
        'ja', 'ar', 'hi', 'ko', 'tr', 'pl', 'vi', 'sv', 'fi',
        'da', 'no', 'he', 'el', 'id', 'th', 'cs', 'hu', 'ro',
        'uk', 'fa', 'sr', 'bg', 'sk', 'sl', 'lt', 'lv', 'et',
        'hr', 'ca', 'eu'
    ]


    while idioma_livro not in idiomas_permitidos:
        print("Idioma inválido. Digite um idioma válido.")
        idioma_livro = input("Digite o idioma do livro (exemplos - pt, en, es, ru, fr): ")


    wanted_book.append(idioma_livro)

    wanted_book[0], flag_author = Check_Author(wanted_book[0], address)
    wanted_book[0], wanted_book[1], wanted_book[2], flag_book = Check_Book(wanted_book[0], wanted_book[1], wanted_book[2], address)

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

        if flag_author == True:
            query = "INSERT INTO autores (autor) VALUES (%s)"
            cursor.execute(query, (wanted_book[0],))
            conn.commit()
            print("\nAutor inserido com sucesso.\n")
            time.sleep(2)

        if flag_book == True:
            query = "INSERT INTO livros (autor, titulo, idioma) VALUES (%s, %s, %s)"
            cursor.execute(query, (wanted_book[0], wanted_book[1], wanted_book[2]))
            conn.commit()

            print("\nLivro inserido com sucesso.\n")
            time.sleep(2)

    except psycopg2.Error as error:
        print("\n\nOcorreu um erro ao conectar ou manipular o banco de dados:", error)
        time.sleep(2)

    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()
