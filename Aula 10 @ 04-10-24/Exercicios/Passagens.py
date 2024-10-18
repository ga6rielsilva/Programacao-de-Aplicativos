def lerMatriz(dimensao):
    mat = [[0] for _ in range(dimensao)]  # Inicializa todas as poltronas como vazias

    for i in range(dimensao):
        if mat[i][0] == 0:  # Verifica se a poltrona está vazia
            mat[i][0] = 1  # Ocupa a poltrona
            print(f"Poltrona {i+1} vendida com sucesso.")
        else:
            print(f"A poltrona {i+1} já está ocupada.")
    return mat