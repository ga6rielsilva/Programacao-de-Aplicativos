while True:
    # Verficiar se o jogador 1 escolheu um número válido
    j1 = int(input("\nPedra, papel ou tesoura? \n0 - Pedra\n1 - Papel\n2 - Tesoura\nJogador #1 > "))
    if j1 < 0 or j1 > 2:
        print("Informe um número válido entre 0 e 2.\n")
        continue

    # Verficiar se o jogador 2 escolheu um número válido
    j2 = int(input("\nPedra, papel ou tesoura? \n0 - Pedra\n1 - Papel\n2 - Tesoura\nJogador #2 > "))
    if j2 < 0 or j2 > 2:
        print("Informe um número válido entre 0 e 2.\n")
        continue

    if j1 == j2:
        print("Empate!")

    elif j1 == 0 and j2 == 1:
        print("\nJogador 2 venceu!\n")
    else:
        print("\nJogador 1 venceu!\n")

    # Verifica se os jogadores desejam jogar novamente
    i = int(input("Deseja jogar novamente? \n0 - Sim\n1 - Não\n> "))
    if i < 0 or i > 1:
        print("Informe um número válido entre 0 e 1.\n")
    if i == 1:
        print("Fim do jogo!")
        break