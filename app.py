from flask import Flask
from routes.fornecedor_routes import fornecedor_bp
from routes.auth_routes import auth_bp
from routes.dashboard_routes import dashboard_bp
from routes.admin_routes import admin_bp

app = Flask(__name__)

app.secret_key = "segredo_senha"

app.register_blueprint(dashboard_bp)
app.register_blueprint(fornecedor_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(admin_bp)

@app.route("/")
def home():
    return "Teste do projeto"


if __name__ == "__main__":
    app.run(debug=True)
