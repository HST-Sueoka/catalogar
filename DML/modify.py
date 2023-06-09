import time
import psycopg2
from support.normalize import normalizar_palavra



def Check_Author(autor_desejado, address):
    print("Verificando a existência do autor.\n")

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
        autores_existentes = cursor.fetchall()

        autores_existentes_normalized = [normalizar_palavra(author[0]) for author in autores_existentes]

        autor_desejado_normalizado = normalizar_palavra(autor_desejado)

        if autor_desejado_normalizado in autores_existentes_normalized:
            index = autores_existentes_normalized.index(autor_desejado_normalizado)
            autor_desejado = autores_existentes[index][0]
            flag_author = False
        else:
            flag_author = True

    except Exception as error:
        print("Ocorreu um erro ao conectar ou manipular o banco de dados:", error)
        time.sleep(3)

    finally:
        if cursor is not None:
            cursor.close()

        if conn is not None:
            conn.close()

    return autor_desejado, flag_author



def Check_Book(autor_desejado, titulo_desejado, idioma_desejado, address):
    print("Verificando a existência do livro.\n")

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
        cursor.execute(query, (autor_desejado,))
        livros_existentes = cursor.fetchall()

        livros_existentes_normalized = [(normalizar_palavra(book[0]), normalizar_palavra(book[1]), normalizar_palavra(book[2])) for book in livros_existentes]

        autor_desejado_normalizado  = normalizar_palavra(autor_desejado)
        titulo_desejado_normalizado = normalizar_palavra(titulo_desejado)
        idioma_desejado_normalizado = normalizar_palavra(idioma_desejado) 
 
        if (autor_desejado_normalizado, titulo_desejado_normalizado, idioma_desejado_normalizado) in livros_existentes_normalized:
            index = livros_existentes_normalized.index((autor_desejado_normalizado, titulo_desejado_normalizado, idioma_desejado_normalizado))
            autor_desejado = livros_existentes[index][0]
            titulo_desejado = livros_existentes[index][1]
            idioma_desejado = livros_existentes[index][2]
            flag_book = False
        else:
            flag_book = True
            

    except Exception as error:
        print("\nOcorreu um erro ao conectar ou manipular o banco de dados:", error)
        time.sleep(3)

    finally:
        if cursor is not None:
            cursor.close()

        if conn is not None:
            conn.close()

    return autor_desejado, titulo_desejado, idioma_desejado, flag_book