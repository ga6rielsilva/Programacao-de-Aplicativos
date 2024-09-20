n = int(input("Digite um número inteiro positivo: "))

numero = 2
divisores = True # Primo é a variável contadora

while (numero <= n - 1) and (divisores):
    if (n % numero == 0): # Se o resto da divisão for zero, o número não é primo
        divisores += 1
    numero += 1

if (divisores == 0):
    print("O número", n, "é primo.")
elif (divisores == 1):
    print("Não é primo. Possui 1 divisor diferente de 1 e", n)
else:
    print("Não é primo. Possui", divisores, "divisores diferentes de 1 e", n)