import locale
from pathlib import Path
import time
from format import format_epub, format_pdf, format_unknown, format_docx, format_txt
from support import dataBase

def Scan_Directory(address, flag):
    
    # Limpar o console
    print("\033c")  

    # Obter diretório para análise
    directory = input("Digite o caminho do diretório a ser analisado: ")

    # Configurar o locale
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

    book_collection = []
    author_collection = []
    file_counter = 0

    print("\n\nIniciando Software\n\n")

    for file_path in Path(directory).rglob('*'):
        if not file_path.is_file():
            continue

        name = file_path.name

        print(f"\nAnalisando o arquivo >>> {name}")

        if name.endswith('.epub'):
            author, title, language = format_epub.process_epub(file_path, name)

        elif name.endswith('.pdf'):
            author, title, language = format_pdf.process_pdf(file_path, name)
        
        elif name.endswith('.docx'):
            author, title, language = format_docx.process_docx(file_path, name)

        elif name.endswith('.txt'):
            author, title, language = format_txt.process_txt(file_path, name)
        
        else:
            author, title, language = format_unknown.process_unknown(file_path, name)

        book_collection.append({'autor': author, 'titulo': title, 'idioma': language})

        v_author = author
        if v_author not in author_collection:
            author_collection.append(v_author)
        
        file_counter = file_counter + 1

    # Ordenar a lista
    book_collection = sorted(book_collection, key=lambda x: locale.strxfrm(x['autor']))

    print(f'\n\nArquivos escaneados = {file_counter}')

    # Adicionar livros ao banco de dados

    time.sleep(3)
    dataBase.commit_scan(book_collection, author_collection, address, flag)

    return
