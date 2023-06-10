
from autenticar.cadastro import cadastrar_usuario
from autenticar.sobre import sobre_software
from dataBase.dataBase_address import input_address
from support.menu import menu
from autenticar.login import realizar_login


address = input_address()


print("[01] - Cadastrar usuário")
print("[02] - Realizar login")
print("[03] - Sobre")

opcao = input("Escolha uma opção: ")

print("\033c")

if opcao == '1':
    print("Cadastro de Usuário")
    nome = input("Digite o nome: ")
    email = input("Digite o e-mail: ")
    senha = input("Digite a senha: ")
    cadastrar_usuario(nome, email, senha, address)

elif opcao == '2':
    print("Login")
    email = input("Digite o e-mail: ")
    senha = input("Digite a senha: ")
    flag, id_usuario = realizar_login(email, senha, address)
    
    if flag == True:
        menu(address, id_usuario)

elif opcao == '3':
    sobre_software()


else:
    print("Opção inválida.")

'''

CREATE TABLE livros (
id SERIAL PRIMARY KEY,
autor VARCHAR(100),
titulo VARCHAR(100),
idioma VARCHAR(25),
FOREIGN KEY (autor) REFERENCES autores(autor)
);


CREATE TABLE autores (
    id SERIAL PRIMARY KEY,
    autor VARCHAR(100) UNIQUE
);



CREATE SEQUENCE usuarios_id_seq START 1;

CREATE TABLE usuarios (
    id INT DEFAULT nextval('usuarios_id_seq'::regclass) PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL
);



CREATE TABLE estante_autores (
    id_usuario INT,
    autor_id INT,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id),
    FOREIGN KEY (autor_id) REFERENCES autores(id),
    PRIMARY KEY (id_usuario, autor_id)
);

CREATE TABLE estante_livros (
    id_usuario INT,
    livro_id INT,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id),
    FOREIGN KEY (livro_id) REFERENCES livros(id),
    PRIMARY KEY (id_usuario, livro_id)
);



'''