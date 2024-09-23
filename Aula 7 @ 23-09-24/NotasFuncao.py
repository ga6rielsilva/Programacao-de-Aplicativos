def lerNota(num):
    notas = []

    for i in range(num):
        dado = float(input("Digite a nota: "))
        notas.append(dado)
    return notas

def calculaMedia(notas):
    soma = 0

    for i in range(len(notas)):
        soma += notas[i]

    return ((soma / len(notas)))

n = int(input("Quantas notas deseja informar? "))

notas = lerNota(n)
print("Notas:", notas)

media = calculaMedia(notas)
print(f"Média: {media:.2f}")