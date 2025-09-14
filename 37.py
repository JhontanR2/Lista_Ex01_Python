lista = {
    "ADS": "Java",
    "GTI": "Python",
    "DMD": "JavaScript"
}

for code in lista.values():
    if code == "Python":
        print("Python encontrado!")
        break
else:
    print("Python não encontrado.")
