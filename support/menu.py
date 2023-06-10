from DML.insert import adicionar_autor, adicionar_livro
from DML.delete import deletar_autor, deletar_livro
from DML.update import Update_Author, Update_Book
from dataBase.dataBase_address import input_address
from exportar.exportar import exportar_dados

from support.scan import escanear_diretorio



def menu (address, id_usuario):
    print("\033c")


    choice = 0

    while choice != 99:

        print("\033c")

        print("[01]  -  Escanear diretório e adicionar somente autores.")
        print("[02]  -  Escanear diretório e adicionar autores & livros.")
        print("[03]  -  Adicionar Autor.")
        print("[04]  -  Adicionar Livro.")
        print("[05]  -  Remover Autor.")
        print("[06]  -  Remover Livro.")
        print("[07]  -  Corrigir Autor.")
        print("[08]  -  Corrigir Livro.")
        print("[25]  -  Inserir o endereço do banco de dados.")
        print("[50]  -  Exportando dados -- Autores.")
        print("[75]  -  Exportando dados -- Autores e Livros.")

        print("[99]  - Sair.")
        choice = input("Opção desejada: ")

        print("\033c")

        if choice == '1':
            print("Escanear diretório e adicionar somente autores.")
            escanear_diretorio(address, False, id_usuario)


        elif choice == '2':
            print("Escanear diretório e adicionar autores & livros.")
            escanear_diretorio(address, True, id_usuario)

        elif choice == '3':
            print("Adicionar Autor")
            adicionar_autor(address, id_usuario)

        elif choice == '4':
            print("Adicionar Livro")
            adicionar_livro(address, id_usuario)

        elif choice == '5':
            print("Remover Autor")
            deletar_autor(address, id_usuario)

        elif choice == '6':
            print("Remover Livro")
            deletar_livro(address, id_usuario)

        elif choice == '7':
            print("Corrigir Autor")
            Update_Author(address, id_usuario)
        elif choice == '8':
            Update_Book(address)
            print("Corrigir Livro")

        elif choice == '99':
            print("Finalizando Programa")

        elif choice == '25':
            print("Inserir o endereço do banco de dados")
            address = input_address()

        elif choice == '50':
            print("Exportando dados -- Autores")
            exportar_dados(address, False)

        elif choice == '75':
            print("Exportando dados -- Autores e Livros")
            exportar_dados(address, True)

        else:
            print("Opção inexistente!!!")












