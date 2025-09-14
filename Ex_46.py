funcionarios = {
    "Jhonatan": 5000,
    "Leticia": 6000,
    "Joao Pedro": 3000,
    "Vanessa": 4000,
    "Dionisio": 7000

}

for nome in funcionarios:
    funcionarios[nome] *= 1.10
    print(f"{nome} - Salario Novo: {funcionarios[nome]}")
    