numeros = [34,53,755,234,532,321,454,643,123,12]
menor = numeros[0]
for numero in numeros:
    if numero < menor:
        menor = numero
print("O menor número da lista é:", menor)  