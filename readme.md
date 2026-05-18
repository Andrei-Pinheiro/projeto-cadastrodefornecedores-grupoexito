# Sistema de Cadastro de Fornecedores

## Sobre o Projeto

Aplicação web desenvolvida para cadastro e manutenção de fornecedores.

O sistema permite:

* cadastro de fornecedores;
* login com CNPJ e senha;
* visualização de dados cadastrados;
* edição de informações;
* sair do sistema;
* listagem administrativa simples dos fornecedores.


# Tecnologias Utilizadas

## Backend

* Python
* Flask
* SQLite3

## Frontend

* HTML5
* Bootstrap 5

# Estrutura do Projeto

* projeto-cadastro-grupoexito/app.py/requirements.txt/database.db

* database/db.py/init_db.py/schema.sql

* routes/auth_routes.py/fornecedor_routes.py/dashboard_routes.py/admin_routes.py/_init__.py

* templates/cadastro.html/login.html/dashboard.html/editar.html/admin.html

* venv/


# Como Executar o Projeto

## 1. Clonar o repositório

```bash
clone LINK DO REPOSITORIO
```

## 2. Criar ambiente virtual

```bash
Terminal: python -m venv venv
```

## 3. Ativar ambiente virtual

### Windows

```bash
Terminal: venv\Scripts\activate
```

## 4. Instalar dependência

```bash
Terminal: pip install -r requirements.txt
```

## 5. Criar banco de dados

```bash
Terminal: python database/init_db.py
```

## 6. Executar aplicação

```bash
python app.py
```

# Rotas do Sistema

/cadastro : cadastro de fornecedor
/login : login de fornecedor
/dashboard : área restrita
/editar : editar dados do fornecedor
/logout : sair do sistema
/admin : listagem administraiva


# Banco de Dados

O projeto utiliza SQLite3.

A estrutura principal no arquivo:

```txt
database/schema.sql
```


# Melhorias Futuras

* criptografia de senha;
* integração com BrasilAPI;
* recuperação de senha;
* melhoria visual do sistema;


# Observações

O projeto foi desenvolvido priorizando:

* organização de código;
* funcionalidades principais do desafio;
* simplicidade de manutenção.

O python + Flask + SQLite + Bootstrap foi escolhida por ser compatível com o meu conhecimento atual utilizado no desenvolvimento do desafio, permitindo a entrega no prazo estipuado, mais organizado e funcional.
