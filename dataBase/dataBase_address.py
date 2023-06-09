from difflib import SequenceMatcher


def input_address():

    try:
        address = []
        address.append(input("Digite o database: "))
        address.append(input("Digite o user: "))
        address.append(input("Digite o password: "))
        address.append(input("Digite o host: "))
        address.append(input("Digite o port: "))

    except Exception as error:
        print("\n\nOcorreu um erro ao conectar ou manipular o banco de dados:", error)


    finally:
        print("\nDados obtidos com sucesso.\n")
        return address


def similar_name_exists(author, existing_authors):
    for existing_author in existing_authors:
        if SequenceMatcher(None, existing_author, author).ratio() >= 0.8:
            return True
    return False