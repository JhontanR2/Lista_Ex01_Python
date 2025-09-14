palavras = ["Eu", "Dormi", "Na", "Praça", "Pensando", "Nela"]
contando = 0

for palavra in palavras:
    if palavra.startswith('P'):
        contando += 1
        print("Qtd de palavras que começam com P: ", contando)