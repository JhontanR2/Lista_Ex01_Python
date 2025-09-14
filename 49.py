paises = {
    "Vaticano": {"capital": "Vaticano", "populacao": "501"},
    "Tuvalu": {"capital": "Funafuti", "populacao": "11.000"},
    "Nauru": {"capital": "Yaren", "populacao": "12.500"},
    "Palau": {"capital": "Ngerulmud", "populacao": "18.000"},
    "San Marino": {"capital": "San Marino", "populacao": "34.000"},
}

for pais, info in paises.items():
    for campo, valor in info.items():
        if campo == "capital":
            print(f"A capital de {pais} é {valor}")
        if campo == "populacao":
            print(f"A populacao de {pais} é {valor}")
    print()
