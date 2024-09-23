def posNeg(numero):
    if numero > 0:
        print("Positivo")
    elif numero < 0:
        print("Negativo")
    else:
        print("Zero")
    
numero = int(input("Digite um número: "))
resultado = posNeg(numero)
print(f"O número {numero} é {resultado}")