import psycopg2
import time

from support.normalize import normalize_word


def commit_scan(book_collection, author_collection, address, flag):
    # Limpar o console
    print("\033c")
    print("\nAnalisando dados coletados\n")

    try:
        # Estabelecer a conexão com o banco de dados
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
        results = cursor.fetchall()

        existing_authors_normalized = [normalize_word(row[0]) for row in results]
        existing_authors_not_normalized = [row[0] for row in results]

        # Conjunto para armazenar as combinações únicas de autor e título processados
        processed_books = set()

        # Inserir os dados válidos na tabela de autores do banco de dados
        for author_item in author_collection:
            normalized_author_item = normalize_word(author_item)

            if normalized_author_item not in existing_authors_normalized:
                # O autor não existe na tabela, realizar a inserção
                query = "INSERT INTO autores (autor) VALUES (%s)"
                cursor.execute(query, (author_item,))
            else:
                print(f"Autor {author_item} já existe na tabela, pulando a inserção.")
                # Modificar o nome do autor para o valor existente no banco de dados
                index = existing_authors_normalized.index(normalized_author_item)
                existing_author = existing_authors_not_normalized[index]
                author_item = existing_author

            # Adicionar autor ao conjunto de autores processados
            processed_books.add((author_item, ""))  # Adicionar apenas o autor no conjunto

        if flag:
            # Obtém os dados existentes na tabela de livros
            query = "SELECT autor, titulo, idioma FROM livros"
            cursor.execute(query)
            results = cursor.fetchall()

            # Inserir os dados válidos na tabela de livros do banco de dados
            for book in book_collection:
                author = book['autor']
                title = book['titulo']
                language = book['idioma']

                normalized_author = normalize_word(author)
                normalized_title = normalize_word(title)

                # Verificar se a combinação de autor, título e idioma já foi processada
                if (normalized_author, normalized_title, language) in processed_books:
                    print(f"Livro '{title}' do autor '{author}' no idioma '{language}' já existe na tabela, pulando a inserção.")
                else:
                    # O livro não existe na tabela, realizar a inserção
                    query = "INSERT INTO livros (autor, titulo, idioma) VALUES (%s, %s, %s)"
                    cursor.execute(query, (author, title, language))

                # Adicionar a combinação de autor, título e idioma ao conjunto de livros processados
                processed_books.add((normalized_author, normalized_title, language))

        conn.commit()
        print("\nDados inseridos com sucesso.\n")
        # Pausa a execução por 5 segundos
        time.sleep(10)

    except psycopg2.Error as error:
        # Confirmar as alterações no banco de dados
        print("\n\nOcorreu um erro ao conectar ou manipular o banco de dados:", error)
        # Pausa a execução por 5 segundos
        time.sleep(10)

    finally:
        # Fechar a conexão com o banco de dados
        if cursor is not None:
            cursor.close()

        if conn is not None:
            conn.close()
