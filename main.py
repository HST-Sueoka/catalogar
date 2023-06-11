
from autenticar.registro import registro
from dataBase.dataBase_connection import address_connection, test_connection


def main():
    print("\033c")
    print("Conexão com o Banco de Dados necessário.\n")
    address = address_connection()
    flag = test_connection(address)

    if flag == True:
        registro(address)

    elif flag == False:
        print("Aplicação encerrada.")


if __name__ == "__main__":
    main()


'''
CREATE TABLE tb_autores (
    id SERIAL PRIMARY KEY,
    autor VARCHAR(100) UNIQUE
);

CREATE TABLE tb_livros (
    id SERIAL PRIMARY KEY,
    autor VARCHAR(100),
    titulo VARCHAR(100),
    idioma VARCHAR(25),
    FOREIGN KEY (autor) REFERENCES tb_autores(autor)
);

CREATE TABLE tb_usuarios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL
);

CREATE TABLE tb_estante_autores (
    id_usuario INT,
    id_autor INT,
    FOREIGN KEY (id_usuario) REFERENCES tb_usuarios(id),
    FOREIGN KEY (autor_id) REFERENCES tb_autores(id),
    PRIMARY KEY (id_usuario, id_autor)
);

CREATE TABLE tb_estante_livros (
    id_usuario INT,
    id_livro INT,
    FOREIGN KEY (id_usuario) REFERENCES tb_usuarios(id),
    FOREIGN KEY (id_livro) REFERENCES tb_livros(id),
    PRIMARY KEY (id_usuario, id_livro)
);


'''