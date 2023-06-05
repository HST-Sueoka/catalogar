import os
from PyPDF2 import PdfReader
from langdetect import detect

def process_pdf(file_path, name):
    try:
        split_name = os.path.splitext(name)[0].split(' - ')
        author = split_name[0]
        title = split_name[1].split(' (')[0] 
        
        reader = PdfReader(file_path)
        content = ''
        for page in reader.pages:
            content += page.extract_text()

        language = detect(content)

        return author, title, language
    
    except Exception as e:
        split_name = os.path.splitext(name)[0].split(' - ')
        author = split_name[0]
        title = split_name[1].split(' (')[0] 
        language = 'unknown'
        
        print(f"Erro ao processar o arquivo {name}: {str(e)}")
        return author, title, language
