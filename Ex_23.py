lista1 = [1,2,3,4,5]
lista2 = [6,7,8,9,10]

resultado = []

for num1 in lista1:
    for num2 in lista2:
        resultado.append(num1 * num2)

        print("Resultado das multiplicações:", resultado)