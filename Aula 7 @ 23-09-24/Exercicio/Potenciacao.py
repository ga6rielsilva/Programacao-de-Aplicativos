import math

def leitorNumero():
    numero = int(input("Informe um número: "))
    return numero

def potencia(base, expoente):
    resultado = math.pow(base, expoente)
    return resultado

num1 = leitorNumero()
num2 = leitorNumero()
print(potencia(num1, num2))