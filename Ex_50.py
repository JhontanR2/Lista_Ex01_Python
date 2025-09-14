hobbies_e_pessoas = {
    "João": ["futebol", "Videogames", "leitura"],
    "Maria": ["dança", "pintura", "ciclismo"],
    "Jhonatan": ["programação", "academia", "leitura"],
    "Ana": ["natação", "viagens", "fotografia"],
    "Carlos": ["corrida", "cinema", "pescar"]
}

print("Pessoas que tem 'leitura' como hobby: ")

for nome, lista_hobbies in hobbies_e_pessoas.items():
    if "leitura" in lista_hobbies:
        print(nome) 