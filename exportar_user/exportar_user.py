import os
import json
import time
import psycopg2

def exportar_dados_user(address, id_usuario):
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

        # Consulta para obter os autores na tabela tb_estante_autores com base no id_usuario
        query_autores = """
        SELECT tb_autores.id, tb_autores.autor
        FROM tb_estante_autores
        JOIN tb_autores ON tb_estante_autores.id_autor = tb_autores.id
        WHERE tb_estante_autores.id_usuario = %s;
        """
        cursor.execute(query_autores, (id_usuario,))
        resultado_autores = cursor.fetchall()

        connection.commit()

        autores_formatados = [{"id": autor[0], "autor": autor[1]} for autor in resultado_autores]

        with open(os.path.join(diretorio_atual, "user_autores.json"), "w", encoding="utf-8") as file:
            json.dump(autores_formatados, file, indent=4, ensure_ascii=False)

        print("Autores coletados com sucesso.")
        time.sleep(2)

        # Consulta para obter os livros na tabela tb_estante_livros com base no id_usuario
        query_livros = """
        SELECT tb_livros.id, tb_livros.autor, tb_livros.titulo, tb_livros.idioma
        FROM tb_estante_livros
        JOIN tb_livros ON tb_estante_livros.id_livro = tb_livros.id
        WHERE tb_estante_livros.id_usuario = %s;
        """
        cursor.execute(query_livros, (id_usuario,))
        resultado_livros = cursor.fetchall()

        livros_formatados = [{"id": livro[0], "autor": livro[1], "titulo": livro[2], "idioma": livro[3]} for livro in resultado_livros]

        with open(os.path.join(diretorio_atual, "user_livros.json"), "w", encoding="utf-8") as file:
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
