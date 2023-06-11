import psycopg2
import time

from suporte.normalize import normalizar_palavra



def commit_scan(colecao_livros, colecao_autores, colecao_livros_normalizados, address, flag):
    print("\033c")
    print("Analisando dados coletados\n")

    try:
        # Estabelecer a conexão com o banco de dados
        connection = psycopg2.connect(
            database=address[0],
            user=address[1],
            password=address[2],
            host=address[3],
            port=address[4]
        )

        # Criar um cursor para executar as consultas
        cursor = connection.cursor()


        # Obtém os autores existentes no banco de dados
        query = "SELECT id, autor FROM tb_autores"
        cursor.execute(query)
        resultado_autores = cursor.fetchall()

        autores_existentes = [(row[0], row[1]) for row in resultado_autores]
        autores_existentes_normalizados = [normalizar_palavra(autor[1]) for autor in autores_existentes]

        for autor in colecao_autores:
            autor_normalizado = normalizar_palavra(autor)
            if autor_normalizado not in autores_existentes_normalizados:
                query = "INSERT INTO tb_autores (autor) VALUES (%s) RETURNING id"
                cursor.execute(query, (autor,))
            else:
                index = autores_existentes_normalizados.index(autor_normalizado)
                autor_existente = autores_existentes[index][1]

                for index, livro_normalizado in enumerate(colecao_livros_normalizados):
                    if autor_normalizado == livro_normalizado[0]:
                        colecao_livros[index][0] = autor_existente


        connection.commit()


        # Obtém os dados existentes na tabela de livros
        if flag:
            query = "SELECT autor, autor, titulo, idioma, id FROM tb_livros"
            cursor.execute(query)
            resultado_livros = cursor.fetchall()

            livros_existentes_normalizados = [[normalizar_palavra(row[0]), normalizar_palavra(row[1]), row[2], row[3]] for row in resultado_livros]

            for autor_normalizado, titulo_normalizado, idioma in colecao_livros_normalizados:
                if [autor_normalizado, titulo_normalizado, idioma] not in livros_existentes_normalizados:
                    index = colecao_livros_normalizados.index([autor_normalizado, titulo_normalizado, idioma])
                    autor = colecao_livros[index][0]
                    titulo = colecao_livros[index][1]
                    idioma = colecao_livros[index][2]
                    query = "INSERT INTO tb_livros (autor, titulo, idioma) VALUES (%s, %s, %s) RETURNING id"
                    cursor.execute(query, (autor, titulo, idioma))
                    livro_id = cursor.fetchone()[0]
                else:
                    livro_id = livros_existentes_normalizados[index][3]

            connection.commit()
            print("Dados inseridos com sucesso.\n")


    except Exception as error:
        # Confirmar as alterações no banco de dados
        print("\n\nOcorreu um erro ao conectar ou manipular o banco de dados:", error)
        # Pausa a execução por 5 segundos
        time.sleep(3)

    finally:
        print("\n\nInserido com sucesso")
        time.sleep(3)

        # Fechar a conexão com o banco de dados
        if cursor is not None:
            cursor.close()

        if connection is not None:
            connection.close()
