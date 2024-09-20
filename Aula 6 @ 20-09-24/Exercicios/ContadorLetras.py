palavra = input("Informe uma palavra: ")
dicionario = {}

for letra in palavra:
    if letra in dicionario:
        dicionario[letra] += 1
    else:
        dicionario[letra] = 1

maisRepetida = max(dicionario, key=dicionario.get)
quantidade = dicionario[maisRepetida]

print(f"A letra '{maisRepetida.upper()}' é a mais repetida, aparecendo {quantidade} vezes.")