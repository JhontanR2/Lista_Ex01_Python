produuto = {
    "cigarro": 12.00,
    "cerveja": 5.00,
    "refrigerante": 4.00,
    "Preservativo": 2.00,
    "Chocolate": 3.00
    
}

total = 0

for preco in produuto.values():
    total += preco

print("Valor total da compra", total)