quantidade = int(input("Informe a quantidade de notas: "))
notas = []

for i in range(quantidade):
    notas.append(float(input(f"Informe a {i+1}ª nota: ")))

media = sum(notas) / quantidade

print(notas)
print(f"A média das notas é {media:.1f}")