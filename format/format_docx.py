import os
from docx import Document
from langdetect import detect

def process_docx(file_path, name):
    try:
        split_name = os.path.splitext(name)[0].split(' - ')
        author = split_name[0]
        title = split_name[1].split(' (')[0] 
        
        doc = Document(file_path)
        content = ' '.join([paragraph.text for paragraph in doc.paragraphs])
        
        language = detect(content)
        
        return author, title, language  
    except Exception as e:
        split_name = os.path.splitext(name)[0].split(' - ')
        author = split_name[0]
        title = split_name[1].split(' (')[0] 
        language = 'unknown'
        
        print(f"Erro ao processar o arquivo {name}: {str(e)}")
        return author, title, language
