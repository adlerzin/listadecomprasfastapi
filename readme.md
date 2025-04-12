# 🧾 Lista de Itens - FastAPI

Este projeto é uma API simples construída com **FastAPI** para gerenciar uma lista de itens. Ele inclui funcionalidades para adicionar, listar, editar, concluir e deletar itens, além de renderizar uma página HTML com Jinja2.

---

## 🚀 Funcionalidades

- 📃 Listar todos os itens
- ➕ Adicionar novos itens
- ✏️ Editar o nome de um item
- ✅ Marcar item como concluído
- ❌ Deletar item da lista
- 📄 Obter informações como estado e quantidade
- 🌐 Página inicial com template HTML

---

## 📦 Requisitos

- Python 3.9+
- FastAPI
- Uvicorn
- Jinja2

---

## 🔧 Instalação

```bash
# Clone o repositório
git clone https://github.com/adlerzin/listadecomprasfastapi.git
cd seu-repo

# Crie e ative um ambiente virtual (opcional, mas recomendado)
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Instale as dependências
pip install fastapi uvicorn jinja2

# Executando a API
uvicorn main:app --reload
```
Acesse: http://localhost:8000