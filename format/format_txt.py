import os
from langdetect import detect

def process_txt(file_path, name):
    try:
        split_name = os.path.splitext(name)[0].split(' - ')
        author = split_name[0]
        title = split_name[1].split(' (')[0] 
        
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        language = detect(content)
        
        return author, title, language
    except Exception as e:
        split_name = os.path.splitext(name)[0].split(' - ')
        author = split_name[0]
        title = split_name[1].split(' (')[0] 
        language = 'unknown'
        
        print(f"Erro ao processar o arquivo {name}: {str(e)}")
        return author, title, language
