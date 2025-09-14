quadrados = {}

for numero in range(1, 11):
    quadrados[numero] = numero ** 2  

for numero, resultado in quadrados.items():
    print(f"O quadrado de {numero} é {resultado}")
print()
