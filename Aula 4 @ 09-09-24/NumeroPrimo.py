n = int(input("Digite um número inteiro positivo: "))

numero = 2
primo = True # Primo é a variável indicadora

while (numero <= n - 1) and (primo):
    if (n % numero == 0): # Se o resto da divisão for zero, o número não é primo
        primo = False
    numero += 1

if (primo):
    print("O número", n, "é primo.")
else:
    print("O número", n, "é primo.")