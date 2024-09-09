# Lógica para calcular o maior e o menor número da lista
def maior_menor(lista):
    maior = lista[0]
    menor = lista[0]
    for elemento in lista:
        # Define o maior valor
        if elemento > maior:
            maior = elemento
        # Define o menor valor
        elif elemento < menor:
            menor = elemento
    return maior, menor

lista = list()
i = 1

# Loop para informar os elementos da lista
while i <= 10:
    elem = int(input("Digite um elemento da lista: 1"))
    # Adiciona o elemento informado ao final da lista
    lista.append(elem)
    i += 1
    print(lista)


maior, menor = maior_menor(lista)
print("\nMaior:", maior)
print("Menor: %i\n" % menor)