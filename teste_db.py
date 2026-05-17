from database.db import get_connection

conn = get_connection()

conn.execute("""
INSERT INTO fornecedores (
    cnpj,
    razao_social,
    nome_fantasia,
    email,
    telefone,
    endereco,
    cidade,
    uf,
    atividade_principal,
    senha
)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", (
    "12345678000199",
    "Empresa Teste",
    "Teste LTDA",
    "teste@email.com",
    "71999999999",
    "Rua Teste",
    "Salvador",
    "BA",
    "Tecnologia",
    "123456"
))

conn.commit()
conn.close()

print("Fornecedor inserido com sucesso!")