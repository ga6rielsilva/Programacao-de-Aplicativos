n = int(input("Digite a quantidade de números: "))
anterior = int(input())

i = 1
ordenado = 0

while (i < n) and (ordenado == 0):
    atual = int(input())
    i = i + 1
    if (atual < anterior):
        ordenado += 1
    anterior = atual

if (ordenado):
    print("A sequência está ordenada.")
else:
    print("A sequência não está ordenada.")