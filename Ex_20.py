numeros = [1,4,5,6,3,6,5,7,3,5]
contador = 0
for numero in numeros:
    if numero == 5:
        contador += 1
        print("O número 5 aparece", contador, "vezes na lista")