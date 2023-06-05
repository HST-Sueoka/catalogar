## Objetivo

O software (Sem nome definido ainda), tem como objetivo o escaneamento de diretórios que contenha e-books, para a elaboração de um catálogo.
Dessa maneira se tem um maior controle dos livros, como também saber quais livros estão presentes no acervo.

&nbsp;

#### CREATE TABLE autores(
#### &nbsp;   autor VARCHAR(100),
#### &nbsp;   PRIMARY KEY (autor)
#### );

&nbsp;

#### CREATE TABLE livros (
#### &nbsp;  id SERIAL PRIMARY KEY,
#### &nbsp;  autor VARCHAR(100),
#### &nbsp;  titulo VARCHAR(100),
#### &nbsp;  idioma VARCHAR(25),
#### &nbsp;  FOREIGN KEY (autor) REFERENCES autores(autor)
#### );



