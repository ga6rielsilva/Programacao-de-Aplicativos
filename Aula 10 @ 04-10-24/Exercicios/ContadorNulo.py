matriz = []
linhas = 10
colunas = 10

print("Informe os valores da matriz:")
for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = int(input(f"Digite o valor para a posição [{i+1}, {j+1}]: "))
        linha.append(valor)
    matriz.append(linha)

contadorNulo = 0
for i in range(linhas):
    for j in range(colunas):
        if matriz[i][j] == 0:
            contadorNulo += 1

print(f"Você informou: {contadorNulo} nulo(s)")