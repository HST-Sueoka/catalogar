import re
import unicodedata

def normalizar_palavra(palavra):
    # Remover acentuações
    palavra = unicodedata.normalize('NFKD', palavra).encode('ASCII', 'ignore').decode('utf-8')

    # Remover espaços, pontos e transformar em lowercase
    palavra = re.sub(r'[\s.]+', '', palavra).lower()

    return palavra