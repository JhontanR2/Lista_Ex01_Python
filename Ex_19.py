numeros = [3,4,54,32,53,64,234,23,52,25]
somapares = 0
contagem_pares = 0
for numero in numeros:
    if numero % 2 == 0:
        somapares += numero
        contagem_pares += 1

        if contagem_pares > 0:
            media = somapares / contagem_pares
            print("A média dos números pares é:", media)
        
