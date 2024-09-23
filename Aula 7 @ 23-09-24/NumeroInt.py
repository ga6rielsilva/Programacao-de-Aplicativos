def lerNumeroInt():
    num = int(input("Digite um número inteiro: "))
    return num

def soma (num1, num2):
    resultado = num1 + num2
    return resultado

n1 = lerNumeroInt()
n2 = lerNumeroInt()
resultado = soma(n1, n2)
print("A soma é:", resultado)

r = lerNumeroInt()
print("O número informado foi:", r)