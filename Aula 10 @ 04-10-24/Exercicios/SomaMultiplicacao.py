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

def somarMatrizes(mat1, mat2):
    tam = len(mat1)

    mat3 = [[0 for j in range(tam)] for i in range(tam)]
    for i in range(tam):
        for j in range(tam):
            mat3[i][j] = mat1[i][j] + mat2[i][j]
    return mat3

def multiplicarMatrizes(mat1, mat2):
    tam = len(mat1)

    mat3 = [[0 for j in range(tam)] for i in range(tam)]
    for i in range(tam):
        for j in range(tam):
            mat3[i][j] = mat1[i][j] * mat2[i][j]
    return mat3

n = int(input("Qual a dimensão das matrizes?: "))
mat1 = lerMatriz(n)
mat2 = lerMatriz(n)

print("Matriz 1:")
imprimirMatriz(mat1)

print("Matriz 2:")
imprimirMatriz(mat2)

somar_matrizes = somarMatrizes(mat1, mat2)

print("Resultado da soma:")
imprimirMatriz(somar_matrizes)

multiplicar_matrizes = multiplicarMatrizes(mat1, mat2)

print("Resultado da multiplicação:")
imprimirMatriz(multiplicar_matrizes)