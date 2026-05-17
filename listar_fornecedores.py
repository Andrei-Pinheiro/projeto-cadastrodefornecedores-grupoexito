from database.db import get_connection

conn = get_connection()

fornecedores = conn.execute(
    "SELECT * FROM fornecedores"
).fetchall()

for fornecedor in fornecedores:
    print(dict(fornecedor))

conn.close()