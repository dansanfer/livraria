from http.client import HTTPException

from fastapi import FastAPI

Livros = [
    "O Senhor dos Anéis",
    "Harry Potter",
    "O Pequeno Príncipe",
    "1984",
    "O Hobbit"
]

app = FastAPI()


# Saudação
@app.get("/saudacao")
async def saudacao():
    return {"message": "Bem vindo à API de Livros!"}


# Listar livros
@app.get("/livros")
async def listar_livros():
    return {"livros": Livros}


# Adicionar livro
@app.post("/livros")
async def adicionar_livro(livro: str):
    Livros.append(livro)
    return {"message": "Livro adicionado com sucesso!"}

@app.put("/livros/{index}")
async def atualizar_livro(index: int, new_livro: str):
    if index > len(Livros) or index < 0:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    Livros[index] = new_livro
    return {"message": "Livro atualizado com sucesso!"}

@app.delete("/livros/{index}")
async def deletar_livro(index: int):
    if index > len(Livros) or index < 0:
        raise HTTPException(status_code=404, detail="Livro não encontrado") 
    Livros.pop(index)
    return {"message": "Livro deletado com sucesso!"}
