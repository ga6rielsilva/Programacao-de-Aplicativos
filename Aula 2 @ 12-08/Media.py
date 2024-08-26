notaA = float(input("Digite a primeira nota: "))
notaB = float(input("Digite a segunda nota: "))

# Calcular a média
mediaFinal = (notaA + notaB) / 2

# Verificação de aprovação
if mediaFinal >= 7.0:
    print("A sua média é de %.1f, portanto, você foi aprovado!" % mediaFinal)
elif mediaFinal >= 5.0 and mediaFinal < 7.0:
    print("A sua média é de %.1f, portanto, você está de recuperação!" % mediaFinal)
else:
    print("A sua média é de %.1f, portanto, você foi reprovado!" % mediaFinal)