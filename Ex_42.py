alunos = {
    "João": [8.5, 9.0],
    "Maria": [7.0, 6.5],
    "Pedro": [9.5, 8.0],
    "Ana": [10.0, 9.5]
}

for aluno, notas in alunos.items():
    media = sum(notas) / len(notas)
    print(f"{aluno} - Média: {media}")
