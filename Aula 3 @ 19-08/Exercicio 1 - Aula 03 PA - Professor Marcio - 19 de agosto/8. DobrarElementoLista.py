def dobrar_lista(lista):
    nova_lista = []
    
    for elemento in lista:
        # Dobra o valor do elemento e adiciona na nova lista
        novo_elemento = elemento * 2
        # Adiciona o valor dobrado ao final da nova lista
        nova_lista.append(novo_elemento) 
    return nova_lista 

lista=list()
i=1

# Loop para informar os elementos da lista
while (i <= 10):
    elem = int(input("Digite um elemento da lista: ")) 
    # Adiciona o elemento informado ao final da lista
    lista.append(elem)
    i+=1 
    
print(lista) 
nova_lista = dobrar_lista(lista)
print(nova_lista)
