cidades = {
    "Gotham": 12300000,
    "Jedha": 5000000,
    "Metropolis": 15000000,
    "Springfield": 300000,
    "Wakanda": 7000000
}

for cidade, populacao in cidades.items():
    if populacao > 1000000:
        print(cidade)
        