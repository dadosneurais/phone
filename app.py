from flask import Flask, request, jsonify, render_template
import requests
from db import get_client_ip, save_log_to_db

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/buscar', methods=['POST'])
def buscar():
    data = request.get_json()
    numero = data.get("telefone")

    if not numero:
        return jsonify({"erro": "Número não fornecido"}), 400

    ip = get_client_ip()
    save_log_to_db(ip, numero)

    payload = {"phone": f"55{numero}"}
    response = requests.post("https://donodozap.com/api/verify", json=payload)

    try:
        json_data = response.json()
        nomes = [item.get("NOME") for item in json_data.get("accounts", [])]
        return jsonify({"nomes": nomes})
    except Exception:
        return jsonify({"erro": "Erro ao processar resposta"}), 500

if __name__ == '__main__':
    app.run(debug=True)
