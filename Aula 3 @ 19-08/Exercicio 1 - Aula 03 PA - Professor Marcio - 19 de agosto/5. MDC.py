# Lógica para calcular o MDC de dois números
def mdc(a, b):
 if b == 0: 
    return a
 else:
    return mdc(b, a % b) 

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

resultado = mdc(num1, num2)
print("MDC:", resultado)