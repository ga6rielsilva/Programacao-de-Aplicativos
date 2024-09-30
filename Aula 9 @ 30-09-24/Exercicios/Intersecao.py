quantidade = int(input("Informe a quantidade de elementos das listas: "))
listaUm = []
listaDois = []
contadorIntersecao = 0

for i in range(quantidade):
    listaUm.append(int(input(f"Primeira lista: Informe o {i + 1}º elemento: ")))
    listaDois.append(int(input(f"Segunda lista: Informe o {i + 1}º elemento: ")))

    if listaUm[i] == listaDois[i]:
        contadorIntersecao += 1

if contadorIntersecao > 0:
    print(f"Quantidade de elementos em comum entre as duas listas: {contadorIntersecao}")
else:
    print("Não há elementos em comum entre as duas listas!")