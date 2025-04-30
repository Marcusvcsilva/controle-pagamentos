# Conversor de Pagamentos com API de Moeda
## 💡 Descrição
Este projeto simula um sistema de controle de pagamentos internacionais, onde cada transação é cadastrada com sua moeda original e automaticamente convertida para BRL (real brasileiro) utilizando uma API pública de câmbio. Os dados são armazenados em um banco de dados SQLite para posterior análise e acompanhamento.

## 🚀 Funcionalidades
- Cadastro de pagamentos com valor, moeda e descrição
- Conversão automática para BRL utilizando a API exchangerate.host
- Armazenamento das transações em banco de dados
- Listagem de pagamentos registrados

## 🛠️ Tecnologias Utilizadas
- Python 3
- SQLite (via sqlite3)
- API exchangerate.host
- Biblioteca `requests`

## ⚙️ Como Executar
1. Clone o repositório:
```bash
git clone https://github.com/seuusuario/controle-pagamentos.git
cd controle-pagamentos

2. Instale as dependências:

pip install requests

3. Execute o arquivo principal 

python src/app.py

📝 Exemplo de Uso

cadastrar_pagamento('Compra AWS', 'USD', 50)
cadastrar_pagamento('Curso online', 'EUR', 30)

📌 Meus objetivos com esse projeto

Iniciar o entendimento/Capacitação para integração com APIs
Continuar/Aprimorar manipulação de banco de dados
Aprimorar/Desenvolver Organização de código com orientação a objetos
Utilizar de boas práticas no desenvolvimento

📚 Meus Próximos Passos (Extras/Próximas releases ☺️)

Criar uma interface interativa com Jupyter Notebook ou Streamlit 
Visualização de relatórios com pandas e matplotlib
Integração com PostgreSQL ou banco em nuvem