import locale
import pathlib
import time
from dataBase.dataBase import commit_scan
from support import format
from support import normalize
from testes import teste

def escanear_diretorio(address, flag):
    print("\033c")
    directory = input("Digite o caminho do diretório a ser analisado: ")
    print("\033c")

    # Configurar o locale
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

    colecao_autores = []
    colecao_autores_normalizados = []
    colecao_livros_normalizados = []
    colecao_livros = []

    print("Iniciando software.\n")

    contador = 0

    for file_path in pathlib.Path(directory).rglob('*'):
        if not file_path.is_file():
            continue

        nome_arquivo = file_path.name

        print(f"Analisando o arquivo >>> {nome_arquivo}")

        if nome_arquivo.endswith('.epub'):
            autor, titulo, idioma = format.process_epub(file_path, nome_arquivo)

        elif nome_arquivo.endswith('.pdf'):
            autor, titulo, idioma = format.process_pdf(file_path, nome_arquivo)

        elif nome_arquivo.endswith('.docx'):
            autor, titulo, idioma = format.process_docx(file_path, nome_arquivo)

        elif nome_arquivo.endswith('.txt'):
            autor, titulo, idioma = format.process_txt(file_path, nome_arquivo)

        else:
            autor, titulo, idioma = format.process_unknown(file_path, nome_arquivo)

        autor_normalizado = normalize.normalizar_palavra(autor)
        titulo_normalizado = normalize.normalizar_palavra(titulo)


        if autor_normalizado not in colecao_autores_normalizados:
            colecao_autores_normalizados.append(autor_normalizado)
            colecao_autores.append(autor)
        else:
            index = colecao_autores_normalizados.index(autor_normalizado)
            autor = colecao_autores[index]


        if [autor_normalizado, titulo_normalizado, idioma] not in colecao_livros_normalizados:
            autor_original = autor
            colecao_livros.append([autor_original, titulo, idioma])
            colecao_livros_normalizados.append([autor_normalizado, titulo_normalizado, idioma])

        contador += 1

    print(f'\nArquivos escaneados = {contador}')
    time.sleep(3)

    teste.gerar_arquivos_json_scan(colecao_livros, colecao_autores, colecao_autores_normalizados, colecao_livros_normalizados)

    commit_scan(colecao_livros, colecao_autores, colecao_autores_normalizados, colecao_livros_normalizados, address, flag)

    return
