from DML_root.delete_root import deletar_autor_root, deletar_livro_root
from DML_root.insert_root import adicionar_autor_root, adicionar_livro_root

from DML_user.delete import deletar_autor_user, deletar_livro_user
from DML_user.insert_user import adicionar_autor_user, adicionar_livro_user

from exportar_user.exportar_user import exportar_dados_user

from exportar_root.exportar_root import exportar_dados_root



from suporte.scan import escanear_diretorio


def menu(address, id_usuario):

    choice = '0'

    while choice != '9999':

        print("\033c")
        print("Menu de Escolhas.\n")

        if id_usuario != 1:
            print("[01]  -  Adicionar Autor.")
            print("[02]  -  Adicionar Livro.")
            print("[03]  -  Remover Autor.")
            print("[04]  -  Remover Livro.")
            print("[05]  -  Exportando dados.")

        else:
            print("[100]  -  Escanear diretório e adicionar somente autores.")
            print("[200]  -  Escanear diretório e adicionar autores & livros.")
            print("[300]  -  Exportar Dados (ROOT)")
            print("[400]  -  Adicionar Autor.")
            print("[500]  -  Adicionar Livro.")
            print("[600]  -  Remover Autor.")
            print("[700]  -  Remover Livro.")

        print("[9999]  - Sair.")
        choice = input("Opção desejada: ")

        print("\033c")

        if id_usuario != 1:
            print()
            if choice == '1':
                print("Adicionar Autor")
                adicionar_autor_user(address, id_usuario)

            elif choice == '2':
                print("Adicionar Livro")
                adicionar_livro_user(address, id_usuario)

            elif choice == '3':
                print("Remover Autor")
                deletar_autor_user(address, id_usuario)

            elif choice == '4':
                print("Remover Livro")
                deletar_livro_user(address, id_usuario)

            elif choice == '5':
                print("Exportando dados")
                exportar_dados_user(address, id_usuario)



        else:
            if choice == '100':
                print("Escanear diretório e adicionar somente autores.")
                escanear_diretorio(address, False)

            elif choice == '200':
                print("Escanear diretório e adicionar autores & livros.")
                escanear_diretorio(address, True)

            elif choice == '300':
                print("Exportar Dados (ROOT)")
                exportar_dados_root(address)

            elif choice == '400':
                print("Adicionar Autor")
                adicionar_autor_root(address)

            elif choice == '500':
                print("Adicionar Livro")
                adicionar_livro_root(address)

            elif choice == '600':
                print("Remover Autor")
                deletar_autor_root(address)

            elif choice == '700':
                print("Remover Livro")
                deletar_livro_root(address)

        if choice == '9999':
            print("Finalizando Programa")

