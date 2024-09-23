def main():
    n1 = lerNumeroInt()
    n2 = lerNumeroInt()
    resultado = soma(n1, n2)
    print("A soma é:", resultado)

def lerNumeroInt():
    num = input("Digite um número inteiro: ")
    return int(num)

def soma (n1, n2):
    resultado = n1 + n2
    return resultado

main()