numeros = [2,3,5,6,7,4,3,5,3,4]

numeros.sort()

n=len(numeros)
if n % 2 == 0:
    mediana = (numeros[n//2 - 1] + numeros[n//2]) / 2
else: 
    mediana = numeros[n//2]

    print("A mediana eh: ", mediana)