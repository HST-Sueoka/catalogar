from difflib import SequenceMatcher


def input_address():
    print("\033c")
    print("Insirá os dados para a conexão\n")

    print()
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

        print("\033c")
        return address
