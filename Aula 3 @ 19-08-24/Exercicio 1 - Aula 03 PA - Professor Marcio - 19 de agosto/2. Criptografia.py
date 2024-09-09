# Solicita ao usuario o deslocamento para realizar a criptografia
deslocamento = int(input("Digite o deslocamento: "))
# Solicita ao usuario o texto para criptografar
texto = input("Digite o texto a ser criptografado: ")
texto_criptografado = ""

# Loop para realizar a criptografia letra por letra
for letra in texto: 
   # Verifica se a letra é maiúscula, e aplica a lógica de criptografia para letras maiusculas
   if letra.isupper():
      letra_criptografada = chr((ord(letra.lower()) + deslocamento - 97) % 26 + 65)
   # Verifica se a letra é minúscula, e aplica a lógica de criptografia para letras minusculas
   elif letra.islower():
      letra_criptografada = chr((ord(letra) + deslocamento - 97) % 26 + 97)
   else:
      # Caso o caractere informado não seja uma letra ele mantem esse caractere
      letra_criptografada = letra

   texto_criptografado += letra_criptografada

print("Texto criptografado:", texto_criptografado)