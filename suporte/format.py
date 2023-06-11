import os
from PyPDF2 import PdfReader
import ebooklib
from ebooklib import epub
from langdetect import detect
from docx import Document


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



def process_epub(file_path, name):
    try:
        split_name = os.path.splitext(name)[0].split(' - ')
        author = split_name[0]
        title = split_name[1].split(' (')[0] 
        
        book = epub.read_epub(file_path)
        content = ''
        for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
            content += item.content.decode('utf-8')

        language = detect(content)

        return author, title, language,
    
    except Exception as e:
        split_name = os.path.splitext(name)[0].split(' - ')
        author = split_name[0]
        title = split_name[1].split(' (')[0] 
        language = 'unknown'
        
        print(f"Erro ao processar o arquivo {name}: {str(e)}")
        return author, title, language


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



def process_unknown(file_path, name):
    try:
        split_name = os.path.splitext(name)[0].split(' - ')
        author = split_name[0]
        title = split_name[1].split(' (')[0] 
        
        book = epub.read_epub(file_path)
        content = ''
        for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
            content += item.content.decode('utf-8')

        language = detect(content)
        
        return author, title, language,  
    except Exception as e:
        split_name = os.path.splitext(name)[0].split(' - ')
        author = split_name[0]
        title = split_name[1].split(' (')[0] 
        language = 'unknown'
                
        print(f"Erro ao processar o arquivo {name}: {str(e)}")
        return author, title, language,


