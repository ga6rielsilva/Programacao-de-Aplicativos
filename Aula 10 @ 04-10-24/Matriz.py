def lerMatriz(dimensao):
    mat = [[] for i in range(dimensao)]

    for i in range(dimensao):
        for j in range(dimensao):
            num = int(input(f"{i+1}, {j+1}: "))
            mat[i].append(num)

    return mat

def imprimirMatriz(mat):
    for linha in mat:
        for numero in linha:
            print(numero, end=" ")
        print()

dimensao = 3 # int(input("Digite a dimensão da matriz: "))
mat = lerMatriz(dimensao)
imprimirMatriz(mat)