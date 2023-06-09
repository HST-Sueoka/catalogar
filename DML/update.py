import time
import psycopg2
from DML.modify import Check_Author


def Update_Author(address):
    autor_desejado_remover = input("Digite o nome do autor que deseja atualizar: ")
    autor_desejado_atualizar = input("Digite o nome do autor que deseja inserir: ")

    autor_desejado_encontrado, flag_author = Check_Author(autor_desejado_remover, address)

    try:
        conn = psycopg2.connect(
            database=address[0],
            user=address[1],
            password=address[2],
            host=address[3],
            port=address[4]
        )

        cursor = conn.cursor()

        if flag_author:
            query = "INSERT INTO autores (autor) VALUES (%s)"
            cursor.execute(query, (autor_desejado_atualizar,))
            conn.commit()

            
        query = "UPDATE livros SET autor = %s WHERE autor = %s"
        cursor.execute(query, (autor_desejado_atualizar, autor_desejado_remover))
        conn.commit()

        if autor_desejado_encontrado != autor_desejado_atualizar:
            query = "DELETE FROM autores WHERE autor = %s"
            cursor.execute(query, (autor_desejado_encontrado,))
            conn.commit()
        
        
    except Exception as error:
        print("\n\nOcorreu um erro ao conectar ou manipular o banco de dados:", error)
        time.sleep(2)

    finally:
        if cursor is not None:
            cursor.close()

        if conn is not None:
            conn.close()






def Update_Book(address):
    id_desejado = input("Digite o ID do livro que deseja atualizar: ")
    
    print("\n*** Agora atualize os livros:\n")
    autor_desejado  = input("Digite o autor do livro: ")
    titulo_desejado = input("Digite o nome do livro: ")
    idioma_desejado = input("Digite o idioma do livro (exemplos - pt, en, es, ru, fr): ")

    idiomas_permitidos = [
        'pt', 'en', 'es', 'fr', 'de', 'it', 'nl', 'ru', 'zh',
        'ja', 'ar', 'hi', 'ko', 'tr', 'pl', 'vi', 'sv', 'fi',
        'da', 'no', 'he', 'el', 'id', 'th', 'cs', 'hu', 'ro',
        'uk', 'fa', 'sr', 'bg', 'sk', 'sl', 'lt', 'lv', 'et',
        'hr', 'ca', 'eu'
    ]

    while idioma_desejado not in idiomas_permitidos:
        print("Idioma inválido. Digite um idioma válido.")
        idioma_desejado = input("Digite o idioma do livro (exemplos - pt, en, es, ru, fr): ")

    
    autor_desejado, flag_author = Check_Author(autor_desejado, address)

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

        if flag_author:
            query = "INSERT INTO autores (autor) VALUES (%s)"
            cursor.execute(query, (autor_desejado,))
            conn.commit()

        
        query = "UPDATE livros SET autor = %s, titulo = %s, idioma = %s WHERE id = %s  "
        cursor.execute(query, (autor_desejado, titulo_desejado, idioma_desejado, id_desejado,))
        conn.commit()


    except psycopg2.Error as error:
        print("\n\nOcorreu um erro ao conectar ou manipular o banco de dados:", error)
        time.sleep(2)
    finally:
        if cursor is not None:
            cursor.close()

        if conn is not None:
            conn.close()
