import os
from dotenv import load_dotenv
from pymongo import MongoClient
from datetime import datetime as dt
from flask import request

# Carrega variáveis de ambiente
load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

# Conexão com o MongoDB
cliente = MongoClient(MONGO_URI)
db = cliente['db_tell']
logs_collection = db['logs']

# Função para obter o IP do cliente
def get_client_ip():
    if 'X-Forwarded-For' in request.headers:
        return request.headers['X-Forwarded-For'].split(',')[0].strip()
    return request.remote_addr

# Função para salvar logs no MongoDB
def save_log_to_db(ip, numero):
    log_data = {
        "ip": ip,
        "timestamp": dt.now().strftime("%Y-%m-%d %H:%M:%S"),
        "telefone": numero
    }
    logs_collection.insert_one(log_data)
