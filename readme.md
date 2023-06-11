# Esquema de Tabelas

A seguir, está o esquema de tabelas atualizado para o projeto:

&nbsp;

## Tabela `tb_autores`

Esta tabela armazena informações sobre os autores dos livros.

| Coluna | Tipo    | Descrição                            |
| ------ | ------- | ------------------------------------ |
| id     | SERIAL  | Identificador único do autor          |
| autor  | VARCHAR | Nome do autor                         |

&nbsp;

## Tabela `tb_livros`

Esta tabela armazena informações sobre os livros.

| Coluna    | Tipo    | Descrição                                       |
| --------- | ------- | ----------------------------------------------- |
| id        | SERIAL  | Identificador único do livro                     |
| autor     | VARCHAR | Chave estrangeira referenciando tb_autores(autor)|
| titulo    | VARCHAR | Título do livro                                  |
| idioma    | VARCHAR | Idioma do livro                                  |

&nbsp;

## Tabela `tb_usuarios`

Esta tabela armazena informações dos usuários.

| Coluna | Tipo    | Descrição                            |
| ------ | ------- | ------------------------------------ |
| id     | SERIAL  | Identificador único do usuário        |
| nome   | VARCHAR | Nome do usuário                       |
| email  | VARCHAR | E-mail do usuário (único)             |
| senha  | VARCHAR | Senha do usuário (criptografada)       |

&nbsp;

## Tabela `tb_estante_autores`

Esta tabela estabelece o relacionamento entre usuários e autores na estante.

| Coluna     | Tipo | Descrição                                               |
| -----------| ---- | ------------------------------------------------------- |
| id_usuario | INT  | Chave estrangeira referenciando tb_usuarios(id)          |
| autor_id   | INT  | Chave estrangeira referenciando tb_autores(id)           |

&nbsp;

## Tabela `tb_estante_livros`

Esta tabela estabelece o relacionamento entre usuários e livros na estante.

| Coluna     | Tipo | Descrição                                               |
| -----------| ---- | ------------------------------------------------------- |
| id_usuario | INT  | Chave estrangeira referenciando tb_usuarios(id)          |
| livro_id   | INT  | Chave estrangeira referenciando tb_livros(id)            |
