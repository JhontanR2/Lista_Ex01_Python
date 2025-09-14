produto = {
    "nome": "Ps5 Pro",
    "preco": 4999.99,
    "disponivel": True
}

for chave in produto:
    if chave == "disponivel":
        if produto[chave]:
            print(f"O produto {produto['nome']} está disponível")
        else:
            print(f"O produto {produto['nome']} está indisponível")