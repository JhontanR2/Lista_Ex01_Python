numeros = [5,-3,-54,44,-53,2,12,-9,0,7]
somanegativos = 0
for numero in numeros:
    if numero < 0:
        somanegativos += numero
print("A soma dos números negativos é:", somanegativos)