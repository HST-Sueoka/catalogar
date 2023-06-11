import time
import psycopg2
from autenticar.sobre import sobre_software
from suporte.menu import menu

def registro(address):
    print("\033c")
    print("[01] - Cadastrar usuário")
    print("[02] - Realizar login")
    print("[03] - Sobre")
    opcao = input("Escolha uma opção: ")

    print("\033c")

    if opcao == '1':
        realizar_sign_up(address)

    elif opcao == '2':
        realizar_sign_in(address)

    elif opcao == '3':
        sobre_software()

    else:
        print("Opção inválida.")


def realizar_sign_in(address):
    print("\033c")
    print("Login\n")
    email = input("Digite o e-mail: ")
    senha = input("Digite a senha: ")
    
    id_usuario = 0

    try:
        connection = psycopg2.connect(
            database=address[0],
            user=address[1],
            password=address[2],
            host=address[3],
            port=address[4]
        )

        cursor = connection.cursor()

        query = "SELECT id FROM tb_usuarios WHERE email = %s AND senha = %s"
        cursor.execute(query, (email, senha))
        resultado = cursor.fetchone()[0]


        if resultado is not None:
            print("Autentificação realizada com sucesso.")
            flag = True
            id_usuario = resultado

        else:
            print("Autentificação inválida.")
            
        
 
    except Exception as error:
        print("\nOcorreu um erro ao conectar ou manipular o banco de dados:", error)

    finally:
        cursor.close()
        connection.close()
    
        if flag == True:
            menu(address, id_usuario)
        else:
            registro(address)


def realizar_sign_up(address):  
    print("\033c")
    print("Cadastro de Usuário\n")
    nome = input("Digite o nome: ")
    email = input("Digite o e-mail: ")
    senha = input("Digite a senha: ")
    try:
        connection = psycopg2.connect(
            database=address[0],
            user=address[1],
            password=address[2],
            host=address[3],
            port=address[4]
        )

        cursor = connection.cursor()

        # Seleciona o usuário pelo email
        cursor.execute('SELECT * FROM tb_usuarios WHERE email = %s', (email,))
        resultado = cursor.fetchone()

        if resultado is None:
            query = "INSERT INTO tb_usuarios (nome, email, senha) VALUES (%s, %s, %s)"
            cursor.execute(query, (nome, email, senha))
            connection.commit()
            print("\nE-mail cadastrado com sucesso.")


        else:
            # O usuário não foi encontrado
            print("\nE-mail já cadastrado.")
        
 


    except Exception as error:
        print("\nOcorreu um erro ao conectar ou manipular o banco de dados:", error)
        time.sleep(3)
            

    finally:
        cursor.close()
        connection.close()
        time.sleep(2)
        return

