from flask import Flask
from routes.fornecedor_routes import fornecedor_bp

app = Flask(__name__)

app.register_blueprint(fornecedor_bp)

@app.route("/")
def home():
    return "Teste do projeto"

if __name__ == "__main__":
    app.run(debug=True)