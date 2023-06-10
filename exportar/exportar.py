import os
import json
import time

import psycopg2

def exportar_dados(address, flag):
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    
    print("\033c")
    print("Exportando dados...\n")
    time.sleep(2)

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


        query = "SELECT * from autores order by autor"
        cursor.execute(query)
        resultado_autores = cursor.fetchall()

        connection.commit()

        autores_formatados = [{"id": nome[0], "autor": nome[1]}for nome in resultado_autores]

        with open(os.path.join(diretorio_atual, "resultado_autores.json"), "w", encoding="utf-8") as file:
            json.dump(autores_formatados, file, indent=4, ensure_ascii=False)


        print("Autores coletados com sucesso.")
        time.sleep(2)

        if flag:
            query = "SELECT id, autor, titulo, idioma FROM livros ORDER BY autor ASC, titulo ASC, idioma ASC, id ASC"
            cursor.execute(query)
            resultado_livros = cursor.fetchall()

            livros_formatados = []
            for livro in resultado_livros:
                livro_formatado = {
                    "id": livro[0],
                    "autor": livro[1],
                    "titulo": livro[2],
                    "idioma": livro[3]
                }
                livros_formatados.append(livro_formatado)

            with open(os.path.join(diretorio_atual, "resultado_livros.json"), "w", encoding="utf-8") as file:
                json.dump(livros_formatados, file, indent=4, ensure_ascii=False)

        print("Livros coletados com sucesso.")
        time.sleep(2)

    except Exception as error:
        # Confirmar as alterações no banco de dados
        print("\n\nOcorreu um erro ao conectar ou manipular o banco de dados:", error)
        time.sleep(3)

    finally:
        if cursor is not None:
            cursor.close()

        if connection is not None:
            connection.close()
