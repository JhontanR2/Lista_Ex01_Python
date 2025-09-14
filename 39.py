paisecapital = {
    "Brasil":"Brasília",
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Peru": "Lima",
    "Bolívia": "La Paz"
}

for pais, capital in paisecapital.items():
    if pais == "Brasil":
        print(f"A capital do Brasil é {capital}.")
        break
else:
    print(f"Brasil não está na lista.")
