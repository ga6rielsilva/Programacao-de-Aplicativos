texto = input("Digite um texto: ")
pontuacao = [".", ",", ";", ":", "!", "?", "(", ")", "[", "]", "{", "}", "<", ">", "/", "\\", "|", "@", "#", "$", "%", "&", "*", "_", "-", "+", "=", "´", "`", "^", "~", "¨", "'", '"']

for i in pontuacao:
    texto = texto.replace(i, "")

texto = texto.split(" ")

print("O texto possuí [", len(texto), "] palavras")