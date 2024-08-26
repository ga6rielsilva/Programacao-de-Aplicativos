# Lógica para ordenar os números da lista
def insertion_sort(lista):
    # Percorrer a lista de números
    for i in range(1, len(lista)):
        chave = lista[i]
        # Define a posição do número anterior
        j = i - 1

        # Loop para ordenar os números
        while j >= 0 and chave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
            lista[j + 1] = chave 

lista=list()
i=1

while i<=10:
    elem = int(input("Digite um elemento da lista:"))
    # Adiciona o elemento ao final da lista
    lista.append(elem) 
    i+=1
    print(lista)
    # Chama a funcão para ordenar a lista
    insertion_sort(lista)
    print(lista)