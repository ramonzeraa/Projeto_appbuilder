# Projeto_appbuilder
# Documentação do Projeto: CRUD de Escola e Aluno

## Objetivo do Desafio

O objetivo deste projeto é desenvolver um sistema CRUD (Create, Read, Update, Delete) para gerenciar informações de escolas e alunos utilizando o **Flask AppBuilder**. O sistema permitirá o cadastro, visualização, edição e exclusão de registros de alunos e escolas.

## Tecnologias Utilizadas

As seguintes tecnologias foram utilizadas neste projeto:

- **Python**: Linguagem de programação principal utilizada no desenvolvimento do backend.
- **Flask**: Microframework para construção de aplicações web em Python.
- **Flask AppBuilder**: Extensão do Flask que facilita a criação de aplicações web com gerenciamento de usuários e autenticação.
- **SQLAlchemy**: ORM (Object-Relational Mapping) utilizado para interagir com o banco de dados.
- **Flask-Migrate**: Extensão do Flask para gerenciar migrações de banco de dados.
- **Logging**: Módulo integrado do Python utilizado para registrar eventos durante a execução do aplicativo.

## Estrutura do Projeto

O projeto está organizado da seguinte forma:


## Modelos

### Aluno

O modelo `Aluno` contém as seguintes propriedades:

- `id`: Identificador único do aluno (chave primária).
- `nome`: Nome do aluno.
- `celular`: Número de celular do aluno.
- `data_nasc`: Data de nascimento do aluno.

### Escola

O modelo `Escola` contém as seguintes propriedades:

- `id`: Identificador único da escola (chave primária).
- `nome`: Nome da escola.
- `endereco`: Endereço da escola.
- `telefone`: Telefone da escola.

## Configuração do Ambiente

Para configurar o ambiente, siga os passos abaixo:

1. Clone o repositório do projeto:

   ```bash
   git clone https://github.com/ramonzeraa/Projeto_appbuilder.git
   flask run
