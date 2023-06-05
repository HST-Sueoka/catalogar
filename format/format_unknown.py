import os
import ebooklib
from ebooklib import epub
from langdetect import detect

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
