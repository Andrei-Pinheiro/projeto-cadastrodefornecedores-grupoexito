from flask import Blueprint, render_template, request
from database.db import get_connection
import sqlite3

fornecedor_bp = Blueprint("fornecedor", __name__)


@fornecedor_bp.route("/cadastro", methods=["GET", "POST"])
def cadastro():

    mensagem = None

    if request.method == "POST":

        cnpj = request.form.get("cnpj")
        razao_social = request.form.get("razao_social")
        nome_fantasia = request.form.get("nome_fantasia")
        email = request.form.get("email")
        telefone = request.form.get("telefone")
        endereco = request.form.get("endereco")
        cidade = request.form.get("cidade")
        uf = request.form.get("uf")
        atividade_principal = request.form.get("atividade_principal")
        senha = request.form.get("senha")

        if not cnpj or not razao_social or not email or not senha:

            mensagem = """
            Preencha os campos obrigatórios:
            CNPJ, Razão Social, Email e Senha.
            """

            return render_template(
                "cadastro.html",
                mensagem=mensagem
            )

        conn = None

        try:

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
            ))

            conn.commit()

            mensagem = "Fornecedor cadastrado com sucesso!"

        except sqlite3.IntegrityError:

            mensagem = "CNPJ já cadastrado!"

        finally:

            if conn:
                conn.close()

    return render_template(
        "cadastro.html",
        mensagem=mensagem
    )
