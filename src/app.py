import os
import sqlite3
import requests
from datetime import datetime

# Garante que a pasta exista
os.makedirs('data', exist_ok=True)

# Conexão com o banco de dados
conn = sqlite3.connect('data/pagamentos.db')
cursor = conn.cursor()

# Criação da tabela (se não existir)
cursor.execute('''
CREATE TABLE IF NOT EXISTS pagamentos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao TEXT,
    moeda TEXT,
    valor REAL,
    valor_brl REAL,
    data TEXT
)
''')

# Classe de conversão
class ConversorMoeda:
    def __init__(self, base='BRL'):
        self.base = base

    def converter_para_brl(self, valor, moeda):
        if moeda == 'BRL':
            return valor
        url = f"https://open.er-api.com/v6/latest/{moeda}"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            if 'rates' in data and 'BRL' in data['rates']:
                taxa = data['rates']['BRL']
                return valor * taxa
            else:
                print("❌ Erro: taxa BRL não encontrado na resposta")
                print("Resposta recebida:", data)
                return 0.0
            
        else: print(f"❌ Erro na API. Código HTTP: {response.status_code}")
        return 0.0

# Função para cadastrar um pagamento
def cadastrar_pagamento(descricao, moeda, valor):
    conversor = ConversorMoeda()
    valor_brl = conversor.converter_para_brl(valor, moeda)
    data_atual = datetime.now().strftime('%Y-%m-%d')

    cursor.execute('''
        INSERT INTO pagamentos (descricao, moeda, valor, valor_brl, data)
        VALUES (?, ?, ?, ?, ?)
    ''', (descricao, moeda, valor, valor_brl, data_atual))
    conn.commit()
    print(f"Pagamento '{descricao}' adicionado com sucesso!")

# Função para listar pagamentos
def listar_pagamentos():
    cursor.execute('SELECT * FROM pagamentos')
    pagamentos = cursor.fetchall()
    if pagamentos:
        for pagamento in pagamentos:
            print(pagamento)
    else:
        print("Nenhum pagamento cadastrado.")

# Execução principal
if __name__ == '__main__':
    cadastrar_pagamento('Compra AWS', 'USD', 50)
    cadastrar_pagamento('Curso online', 'EUR', 30)

    print("\nPagamentos cadastrados:")
    listar_pagamentos()
