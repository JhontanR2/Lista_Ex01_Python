estoque = {
    "Nike": 7,
    "Adidas": 9,
    "Havaianas": 13,
    "All Star": 14,
    "Vans": 12
}

for produto, quantidade in estoque.items():
    if quantidade < 10:
        print(f"{produto}: Estoque baixo!")
