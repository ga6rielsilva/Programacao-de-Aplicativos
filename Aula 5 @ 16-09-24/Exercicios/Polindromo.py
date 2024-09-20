texto = input("Digite um texto: ")
texto = texto.lower().replace(" ", "")
pontuacao = [".", ",", ";", ":", "!", "?"]

for i in pontuacao:
    texto = texto.replace(i, "")

texto_inventido = texto[::-1]

if texto_inventido == texto:
    print("É um polindromo")
else:
    print("Não é um polindromo")