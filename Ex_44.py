livros = [
    {"titulo": "Harry Potter e a Pedra Filosofal", "autor": "J.K. Rowling"},
    {"titulo": "Memórias Póstumas de Brás Cubas", "autor": "Machado de Assis"},
    {"titulo": "Star Wars: Uma Nova Esperança", "autor": "George Lucas"},
    {"titulo": "Dom Casmurro", "autor": "Machado de Assis"},
    {"titulo": "O Hobbit", "autor": "J.R.R. Tolkien"}
]

for livro in livros:
    if livro["autor"] == "Machado de Assis":
        print(livro["titulo"])