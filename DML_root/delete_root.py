import time
import psycopg2

from suporte.modify import Check_Author, Check_Book


def deletar_autor_root(address):

    autor_desejado = input("Digite o autor que deseja deletar: ")
    autor_desejado, id_autor, flag_author = Check_Author(autor_desejado, address)

    if flag_author == True and id_autor != 0:

        contador = 0

        try:
            conn = psycopg2.connect(
                database=address[0],
                user=address[1],
                password=address[2],
                host=address[3],
                port=address[4]
            )
            cursor = conn.cursor()

            # Remover dados das estantes
            query = "SELECT id FROM tb_livros WHERE autor = %s"
            cursor.execute(query, (autor_desejado,))
            resultado_livro = cursor.fetchall()

            query = "SELECT id_livro FROM tb_estante_livros"
            cursor.execute(query)
            resultado_livro_de_usuarios = cursor.fetchall()

            for livro_usuario in resultado_livro_de_usuarios:
                if livro_usuario in resultado_livro:
                    query = "DELETE FROM tb_estante_livros WHERE id_livro = %s"
                    cursor.execute(query, (livro_usuario,))
                    contador += 1

            print(f"\n{contador} livros removidos da estante de livros.\n")
            conn.commit()

            query = "DELETE FROM tb_estante_autores WHERE id_autor = %s;"
            cursor.execute(query, (id_autor,))
            print(f"\n{autor_desejado} removido da sua estante de autores.\n")
            conn.commit()

            contador = 0



            # Remover dados da Tabela Principal
            for livro_usuario in resultado_livro:
                query = "DELETE FROM tb_livros WHERE id = %s"
                cursor.execute(query, (livro_usuario,))
                contador += 1

            print(f"\n{contador} livros removidos da Tabela Livros.\n")
            conn.commit()

            query = "DELETE FROM tb_autores WHERE id = %s;"
            cursor.execute(query, (id_autor,))
            print(f"\n{autor_desejado} removido da Tabela Autores.\n")
            conn.commit()

        except psycopg2.Error as error:
            print("\nOcorreu um erro ao conectar ou manipular o banco de dados:", error)
            time.sleep(3)

        finally:
            if cursor is not None:
                cursor.close()

            if conn is not None:
                conn.close()
    else:
        print("Autor não está presente no Banco de Dados.")

    time.sleep(3)
    return



def deletar_livro_root(address):

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

        if flag_book == True and id_livro != 0:

            query = "DELETE FROM tb_estante_livros WHERE id_livro = %s;"
            cursor.execute(query, (id_livro,))
            conn.commit()

            query = "DELETE FROM tb_livros WHERE id_livro = %s;"
            cursor.execute(query, (id_livro,))
            conn.commit()

            print(f"\n{livro_desejado[0]} - {livro_desejado[1]} ({livro_desejado[2]}) deletado no Banco de Dados.\n")
        else:
            print(f"\n{livro_desejado[0]} - {livro_desejado[1]} ({livro_desejado[2]}) não está presente no Banco de Dados.\n")

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

