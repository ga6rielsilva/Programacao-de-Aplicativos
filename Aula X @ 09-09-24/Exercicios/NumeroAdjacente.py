n = int(input("Informe a quantidade de números: "))
if (n <= 1):
    print("Os números não são adjacentes.")
    exit()

numero = int(input())
i = 1
adjacente = True

for i in range(n):
    atual = int(input())
    i += 1

    if (atual != numero):
        adjacente = False
    anterior = atual

if (adjacente):
    print("Os números são adjacentes.")
else:
    # 1 também deve ser considerado não adjacente
    print("Os números não são adjacentes.")