numeros = []

# Loop para solicitar 10 números inteiros ao usuário
for i in range(10):
    try:
        numero = int(input("Digite um número inteiro: "))
        numeros.append(numero)
    except ValueError:
        print("Entrada inválida!!!")

# Calcula a soma e a média dos números
soma = sum(numeros)
media = soma / len(numeros)

# Imprime a soma e a média
print("\nSoma: %.2f" % soma)
print("Média: %.2f\n" % media)