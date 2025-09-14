numeros = [1,2,3,4,5,1,6,7,8,4,6,9,10,1,5]
numeros_unicos = []
for numero in numeros:
    if numero not in numeros_unicos:
        numeros_unicos.append(numero)
        print("Lista com N° unicos", numeros_unicos)
        