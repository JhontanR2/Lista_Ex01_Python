nomes = ["ana", "bob", "charlie", "denise", "eva"]
nomesgrandes = []
for nome in nomes:
    if len(nome) > 5:
        nomesgrandes.append(nome)

        print()("Nomes com mais de 5 letras:", nomesgrandes)