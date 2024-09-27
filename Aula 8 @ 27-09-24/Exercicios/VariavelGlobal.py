contador = 0
lista = []

def incrementar_contador():
    global contador
    contador += 1
    return contador

def exibir_contador():
    global contador
    return contador

def adicionar_na_lista():
    global lista
    n = int(input("Informe a quantidade de itens para adicionar à lista: "))
    
    for i in range(n):
        item = input("Informe o item a ser adicionado à lista: ")
        lista.append(item)
    return lista

def exibir_lista():
    global lista
    return lista

def main():
    adicionar_na_lista()
    print("Itens da lista: ", exibir_lista())
    incrementar_contador()
    print("Contador atualizado", exibir_contador())
    incrementar_contador()
    print("Contador atualizado", exibir_contador())
    print("Valor atual do contador:", exibir_contador())
main()
