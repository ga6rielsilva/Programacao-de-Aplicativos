frutas = "Maça", "Banana", "Laranja"
valor = {"Maça": 5.00, "Banana": 2.50, "Laranja": 3.00}

for i in frutas:
    print(f"Fruta: {i} - Preço: R${valor[i]:.2f}")