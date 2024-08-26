# Lógica para obter o último elemento da lista
def obter_ultimo_elemento(lista):
    if lista:
        return lista[-1]
    else:
        return None 

lista=list()
i=1

while i<=5: 
    elem = int(input("Digite um elemento da lista: "))
    # Adiciona o elemento ao final da lista
    lista.append(elem)
    i+=1 
    print(lista) 
    # Chama a função para obter o último elemento da lista
    ultimo_elemento = obter_ultimo_elemento(lista) 
    print("Último elemento da lista:", ultimo_elemento)