frase = "O Palmeiras nao tem mundial"
frase = frase.upper()

frequencia = {}

for letra in frase:
    if letra.isalpha():
        frequencia[letra] = frequencia.get(letra, 0) + 1

for letra, qtd in frequencia.items():
    if qtd == 1:
        print(f"{letra} = {qtd} ocorrência")
    else:
        print(f"{letra} = {qtd} ocorrências")
