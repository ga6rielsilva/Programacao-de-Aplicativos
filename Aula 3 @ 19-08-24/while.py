qtd = 0
soma = 0
valor = float(input("Digite um valor: "))

# Caso um número negativo seja digitado, o loop é interrompido
while valor > 0.0:
    soma += valor
    qtd += 1
    valor = float(input("Digite um valor: "))

media = soma / qtd

print("\nA soma dos valores digitados é: %.2f" % soma)
print("A quantidade de valores digitados é:", qtd)
print("A média dos valores digitados é: %.2f\n" % media)
