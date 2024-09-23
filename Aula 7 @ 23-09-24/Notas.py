# Mostra as notas
notas = []
n = int(input("Quantas notas deseja informar? "))

for i in range(n):
    dado = float(input())
    notas.append(dado)

print(notas)

# Calcula a média
soma = 0

for i in range(len(notas)):
    soma += notas[i]

media = soma / n

print(f"Média: {media:.2f}")