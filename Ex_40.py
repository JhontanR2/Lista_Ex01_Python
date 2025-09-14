frutas = {
    "Banana": "Amarela",
    "Maçã": "Vermelhaa",
    "Uva": "Roxa",
    "Laranja": "Laranha",
    "Pera": "Verde"

}

frutas["Goiaba"] = "Verde"

for fruta, cor in frutas.items():
    print(fruta, "->", cor)