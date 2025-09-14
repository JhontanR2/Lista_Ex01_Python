notas = [7.5, 8.0, 6.5, 9.0, 5.5]
contar = 0 
for nota in notas:
    if nota >= 7:
        contar += 1
print("Número de nota maiores ou iguais a 7:", contar)