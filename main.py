# Importações necessárias do FastAPI, sistema de templates e manipulação de data/hora
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime

# Instância do FastAPI
app = FastAPI()

# Diretório onde estão os templates HTML (Jinja2)
templates = Jinja2Templates(directory="templates")

# Lista onde serão armazenados os itens
items = []

# Classe que representa um item (modelo básico)
class item_novin:
    nome = "item"
    id = 0
    estado = 0  # 0 = pendente, 1 = concluído
    quantidade = 0
    data = ""  # Data de criação

# Rota principal (renderiza um template HTML)
@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "nome": "Adler"})

# Retorna a lista de todos os itens
@app.get("/items")
def get_items():
    return items

# Adiciona um novo item à lista
@app.post("/add")
def add_item(item: str, quantidade: int):
    item_novo = item_novin()
    item_novo.nome = item
    item_novo.id = len(items)
    item_novo.quantidade = quantidade

    # Formata a data atual
    agora = datetime.now()
    item_novo.data = agora.strftime("%d/%m/%Y %H:%M")

    items.append(item_novo)
    return item_novo.id  # Retorna o ID do novo item

# Retorna um item específico pelo ID
@app.get("/items/{item_id}")
def get_item(item_id: int):
    return items[item_id]

# Retorna o estado (pendente ou concluído) de um item
@app.get("/estado/{item_id}")
def get_state(item_id: int):
    return items[item_id].estado

# Marca um item como concluído
@app.post("/concluir")
def concluir_item(item_id: int):
    items[item_id].estado = 1  # 1 = concluído
    return items[item_id].estado

# Retorna a quantidade de um item específico
@app.get("/quantidade/{item_id}")
def get_quantity(item_id: int):
    return items[item_id].quantidade

# Deleta um item da lista pelo ID
@app.delete("/deletar/{item_id}")
def deletar_item(item_id: int):
    items.pop(item_id)
    return items  # Retorna a nova lista após remoção

# Edita um campo específico de um item (por enquanto, só o nome)
@app.post("/editar/{item_id}/{categoria}/{valor}")
def editar_item(item_id: int, categoria: str, valor: str):
    if categoria == "nome":
        items[item_id].nome = valor
        return items[item_id].nome
