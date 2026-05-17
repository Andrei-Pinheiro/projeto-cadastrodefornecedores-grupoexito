CREATE TABLE IF NOT EXISTS fornecedores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cnpj TEXT unique NOT NULL,
    razao_social TEXT NOT NULL,
    nome_fantasia TEXT,
    email TEXT NOT NULL,
    telefone TEXT,
    endereco TEXT,
    cidade TEXT,
    uf TEXT,
    atividade_principal TEXT,
    senha TEXT NOT NULL,
    situacao_cadastral TEXT

);