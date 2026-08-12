# Microblog

Projeto pessoal de um blog simples, construído com **Python** e **Flask**. A ideia é usar essa aplicação como espaço de prática de desenvolvimento web e, aos poucos, evoluir para um portfólio mais completo.

> 🚧 **Em desenvolvimento** — o projeto ainda está nos estágios iniciais e novas funcionalidades serão adicionadas com o tempo.

## Sobre o projeto

O Microblog é uma aplicação web onde usuários podem publicar pequenos textos (posts), semelhante a uma rede social simplificada. Por enquanto o foco está em estruturar a base da aplicação com Flask, templates Jinja2 e boas práticas de organização de código.

## Tecnologias

- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Jinja2](https://jinja.palletsprojects.com/) (templates)
- [python-dotenv](https://github.com/theskumar/python-dotenv) (variáveis de ambiente)

## Estrutura do projeto

```
Microblog/
├── app/
│   ├── __init__.py       # criação e configuração da aplicação Flask
│   ├── routes.py         # rotas da aplicação
│   └── templates/        # templates HTML (Jinja2)
├── microblog.py          # ponto de entrada da aplicação
├── requirements.txt      # dependências do projeto
└── .env                  # variáveis de ambiente (não versionado)
```

## Como executar localmente

### Pré-requisitos

- Python 3.10+ instalado

### Passo a passo

```bash
# 1. Clone o repositório
git clone https://github.com/pedrohfs9/Microblog.git
cd Microblog

# 2. Crie e ative um ambiente virtual
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Linux/macOS

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Configure as variáveis de ambiente
# crie um arquivo .env na raiz do projeto com:
# FLASK_APP=microblog.py

# 5. Execute a aplicação
flask run
```

A aplicação ficará disponível em `http://localhost:5000`.

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
