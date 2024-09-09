def lernotas():
    nota = float(input("Digite a nota: "))
    return nota

def resultado (notaUm, notaDois):
    media = notaUm + notaDois / 2
    
    print ("Primeira nota: ", notaUm)
    print ("Segunda nota: ", notaDois)
    print ("Média: ", media)

    if media >= 7:
        print ("Aprovado")
    else:
        print ("Reprovado")
    
a = lernotas()
b = lernotas()
resultado(a, b)