palavras = ["bebida", "Sexo","Dinheiro","Futebol","Carro"]
vogais = "aeiouAEIOU"
totalvogais = 0
for palavra in palavras:
    for letra in palavra:
        if letra in vogais:
            totalvogais += 1
            print("O número total de vogais é:", totalvogais)
            