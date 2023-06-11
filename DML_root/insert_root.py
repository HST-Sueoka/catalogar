import time
import psycopg2

from suporte.modify import Check_Author, Check_Book


def adicionar_autor_root(address):

    autor_desejado = input("Digite o autor desejado: ")
    autor_desejado, id_autor, flag_author = Check_Author(autor_desejado, address)

    if flag_author == False and id_autor == 0:
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

            query = "INSERT INTO tb_autores (autor) VALUES (%s);"
            cursor.execute(query, (autor_desejado,))
            conn.commit()

            print(f"\n{autor_desejado} adicionado ao banco de dados.\n")

        except psycopg2.Error as error:
            print("\nOcorreu um erro ao conectar ou manipular o banco de dados:", error)
            time.sleep(3)

        finally:
            if cursor is not None:
                cursor.close()

            if conn is not None:
                conn.close()
    else:
        print("Autor está presente no Banco de Dados.")

    time.sleep(3)
    return


def adicionar_livro_root(address):

    livro_desejado = [
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

    livro_desejado.append(idioma_livro)
    livro_desejado[0], id_autor, flag_author = Check_Author(livro_desejado[0], address)
    livro_desejado[0], livro_desejado[1], livro_desejado[2], id_livro, flag_book = Check_Book(livro_desejado[0], livro_desejado[1], livro_desejado[2], address)

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

        if flag_author == False and id_autor == 0:
            query = "INSERT INTO tb_autores (autor) VALUES (%s);"
            cursor.execute(query, (livro_desejado[0],))
            conn.commit()

            print(f"\nAutor {livro_desejado[0]} inserido no Banco de Dados.\n")

        else:
            print("Autor está presente no Banco de Dados.")

        if flag_book == False and id_livro == 0:
            query = "INSERT INTO tb_livros (autor, titulo, idioma) VALUES (%s, %s, %s);"
            cursor.execute(query, (livro_desejado[0], livro_desejado[1], livro_desejado[2],))
            conn.commit()

            print(f"\n{livro_desejado[0]} - {livro_desejado[1]} ({livro_desejado[2]}) inserido no Banco de Dados.\n")
        else:
            print(f"\n{livro_desejado[0]} - {livro_desejado[1]} ({livro_desejado[2]}) já está presente no Banco de Dados.\n")


    except psycopg2.Error as error:
        print("\n\nOcorreu um erro ao conectar ou manipular o banco de dados:", error)
        time.sleep(3)

    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()

    time.sleep(5)
    return
