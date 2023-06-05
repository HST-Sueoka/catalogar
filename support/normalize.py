import re
import unicodedata

def normalize_word(word):
    # Remover acentuações
    word = unicodedata.normalize('NFKD', word).encode('ASCII', 'ignore').decode('utf-8')

    # Remover espaços, pontos e transformar em lowercase
    word = re.sub(r'[\s.]+', '', word).lower()

    return word