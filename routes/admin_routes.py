from flask import Blueprint, render_template
from database.db import get_connection

admin_bp = Blueprint("admin", __name__)


@admin_bp.route("/admin")
def admin():

    conn = get_connection()

    fornecedores = conn.execute("""
        SELECT *
        FROM fornecedores
    """).fetchall()

    conn.close()

    return render_template(
        "admin.html",
        fornecedores=fornecedores
    )