palavras = ["python", "java", "csharp", "javascript", "ruby"]
palavras_invertidas = []
for palavra in palavras:
    palavras_invertidas.append(palavra[::-1])
print("Palavras originais:", palavras)
print("Palavras invertidas:", palavras_invertidas)