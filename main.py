from support.database_address import input_address
from support.scan import Scan_Directory


print("\033c")

choice = 0

while choice != 99:

    print("\033c")

    print("[01]  - Escanear diretório e adicionar autores & livros.")
    print("[02]  - Escanear diretório e adicionar somente autores.")
    print("[03]  - Adicionar Autor.")
    print("[04]  - Adicionar Livro.")
    print("[05]  - Remover Autor.")
    print("[06]  - Remover Livro.")
    print("[07]  - Corrigir Autor.")
    print("[08]  - Corrigir Livro.")
    print("[25]  - Inserir o endereço do banco de dados.")
    print("[99]  - Sair.")
    choice = int(input("Opção desejada: "))

    print("\033c")

    if choice == 1:
        print("Escanear diretório e adicionar autores & livros.")
        Scan_Directory(address, True)

    elif choice == 2:
        print("Escanear diretório e adicionar somente autores.")
        Scan_Directory(address, False)

    elif choice == 3:
        print("Adicionar Autor")

    elif choice == 4:
        print("Adicionar Livro")

    elif choice == 5:
        print("Remover Autor")

    elif choice == 6:
        print("Remover Livro")

    elif choice == 7:
        print("Corrigir Autor")

    elif choice == 8:
        print("Corrigir Livro")

    elif choice == 99:
        print("Finalizando Programa")

    elif choice == 25:
        print("Inserir o endereço do banco de dados")
        address = input_address()

    else:
        print("Opção inexistente!!!")


'''

CREATE TABLE livros (
id SERIAL PRIMARY KEY,
autor VARCHAR(100),
titulo VARCHAR(100),
idioma VARCHAR(25),
FOREIGN KEY (autor) REFERENCES autores(autor)
);

CREATE TABLE autores(
autor VARCHAR(100),
PRIMARY KEY (autor)
);

'''