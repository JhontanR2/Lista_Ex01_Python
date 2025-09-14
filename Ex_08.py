numeros = [34,53,755,234,532,321,454,643,123,12]
maior = numeros[0]
for numero in numeros:
    if numero > maior:
        maior = numero
print("O maior número da lista é:", maior)  