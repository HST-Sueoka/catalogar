import os
import json

def gerar_arquivos_json_scan(colecao_livros, colecao_autores, colecao_autores_normalizados, colecao_livros_normalizados):
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))


    with open(os.path.join(diretorio_atual, "colecao_autores.json"), "w", encoding="utf-8") as file:
        json.dump(colecao_autores, file, indent=4, ensure_ascii=False)

    with open(os.path.join(diretorio_atual, "colecao_autores_normalizados.json"), "w", encoding="utf-8") as file:
        json.dump(colecao_autores_normalizados, file, indent=4, ensure_ascii=False)

    with open(os.path.join(diretorio_atual, "colecao_livros_normalizados.json"), "w", encoding="utf-8") as file:
        json.dump(colecao_livros_normalizados, file, indent=4, ensure_ascii=False)

    with open(os.path.join(diretorio_atual, "colecao_livros.json"), "w", encoding="utf-8") as file:
        json.dump(colecao_livros, file, indent=4, ensure_ascii=False)

