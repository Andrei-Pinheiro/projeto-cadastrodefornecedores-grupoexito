from flask import Blueprint, render_template, request, session, redirect
from database.db import get_connection

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    mensagem = None

    if request.method == "POST":

        cnpj = request.form.get("cnpj")
        senha = request.form.get("senha")

        conn = get_connection()

        fornecedor = conn.execute("""
            SELECT * FROM fornecedores
            WHERE cnpj = ? AND senha = ?
        """, (
            cnpj,
            senha
        )).fetchone()

        conn.close()

        if fornecedor:

            session["fornecedor_id"] = fornecedor["id"]

            return redirect("/dashboard")

        else:

            mensagem = "CNPJ ou senha inválidos!"

    return render_template(
        "login.html",
        mensagem=mensagem
    )


@auth_bp.route("/logout")
def logout():

    session.clear()

    return redirect("/login")
