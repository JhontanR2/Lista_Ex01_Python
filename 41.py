agenda = {
    "Ted": 30,
    "Robin": 28,
    "Barney": 30,
    "Marshal": 29,
    "Lily": 30
}

velhos = []

for nome, idade in agenda.items():
    if idade >= 30:
        velhos.append(nome)

print(velhos)
