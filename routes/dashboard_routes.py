from flask import Blueprint, render_template, session, redirect, request
from database.db import get_connection

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/dashboard")
def dashboard():

    if "fornecedor_id" not in session:
        return redirect("/login")

    conn = get_connection()

    fornecedor = conn.execute("""
        SELECT * FROM fornecedores
        WHERE id = ?
    """, (
        session["fornecedor_id"],
    )).fetchone()

    conn.close()

    return render_template(
        "dashboard.html",
        fornecedor=fornecedor
    )


@dashboard_bp.route("/editar", methods=["GET", "POST"])
def editar():

    if "fornecedor_id" not in session:
        return redirect("/login")

    conn = get_connection()

    fornecedor = conn.execute("""
        SELECT * FROM fornecedores
        WHERE id = ?
    """, (
        session["fornecedor_id"],
    )).fetchone()

    mensagem = None

    if request.method == "POST":

        email = request.form.get("email")
        telefone = request.form.get("telefone")
        endereco = request.form.get("endereco")
        cidade = request.form.get("cidade")
        uf = request.form.get("uf")

        conn.execute("""
            UPDATE fornecedores
            SET
                email = ?,
                telefone = ?,
                endereco = ?,
                cidade = ?,
                uf = ?
            WHERE id = ?
        """, (
            email,
            telefone,
            endereco,
            cidade,
            uf,
            session["fornecedor_id"]
        ))

        conn.commit()

        mensagem = "Dados atualizados com sucesso!"

        fornecedor = conn.execute("""
            SELECT * FROM fornecedores
            WHERE id = ?
        """, (
            session["fornecedor_id"],
        )).fetchone()

    conn.close()

    return render_template(
        "editar.html",
        fornecedor=fornecedor,
        mensagem=mensagem
    )