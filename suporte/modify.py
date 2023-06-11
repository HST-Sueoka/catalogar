import time
import psycopg2
from suporte.normalize import normalizar_palavra



def Check_Author(autor_desejado, address):
    print("\nVerificando a existência do autor.\n")
    flag_author = False
    id_autor = 0

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
        query = "SELECT id, autor FROM tb_autores"
        cursor.execute(query)
        autores_existentes = cursor.fetchall()

        autor_desejado_normalizado = normalizar_palavra(autor_desejado)

        for autor in autores_existentes:
            if normalizar_palavra(autor[1]) == autor_desejado_normalizado:
                autor_desejado = autor[1]
                id_autor = autor[0]
                flag_author = True
                break

    except Exception as error:
        print("Ocorreu um erro ao conectar ou manipular o banco de dados:", error)
        time.sleep(3)

    finally:
        if cursor is not None:
            cursor.close()

        if conn is not None:
            conn.close()

    return autor_desejado, id_autor, flag_author





def Check_Book(autor_desejado, titulo_desejado, idioma_desejado, address):
    print("\nVerificando a existência do livro.\n")

    flag_book = False
    id_livro = 0

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
        query = "SELECT autor, titulo, idioma, id FROM tb_livros Where autor = %s"
        cursor.execute(query, (autor_desejado,))
        livros_existentes = cursor.fetchall()

        livros_existentes_normalized = [(normalizar_palavra(book[0]), normalizar_palavra(book[1]), normalizar_palavra(book[2]), book[3]) for book in livros_existentes]

        autor_desejado_normalizado  = normalizar_palavra(autor_desejado)
        titulo_desejado_normalizado = normalizar_palavra(titulo_desejado)
        idioma_desejado_normalizado = normalizar_palavra(idioma_desejado) 
 
 
        for livro in livros_existentes_normalized:
            if livro[:3] == (autor_desejado_normalizado, titulo_desejado_normalizado, idioma_desejado_normalizado):
                index = livros_existentes_normalized.index(livro)
                autor_desejado = livros_existentes[index][0]
                titulo_desejado = livros_existentes[index][1]
                idioma_desejado = livros_existentes[index][2]
                id_livro = livros_existentes[index][3]
                flag_book = True
                break
            

    except Exception as error:
        print("\nOcorreu um erro ao conectar ou manipular o banco de dados:", error)
        time.sleep(3)

    finally:
        if cursor is not None:
            cursor.close()

        if conn is not None:
            conn.close()

    return autor_desejado, titulo_desejado, idioma_desejado, id_livro, flag_book