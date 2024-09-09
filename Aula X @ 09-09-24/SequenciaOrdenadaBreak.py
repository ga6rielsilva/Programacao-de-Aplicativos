###########################
# EXEMPLO COM BREAK E FOR #
###########################

n = int(input("Digite a quantidade de números: "))
anterior = int(input())

i = 1
ordenado = True

for i in range(n - 1):
    atual = int(input())
    i = i + 1
    if (atual < anterior):
        ordenado = False
    anterior = atual

if (ordenado):
    print("A sequência está ordenada.")
else:
    print("A sequência não está ordenada.")