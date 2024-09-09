# Função para calcular o fatorial de um número
def fatorial(n, resultado=1):
    if n == 0 or n == 1:
        # caso base 
        return resultado 
    else:
        # passo recursivo 
        return fatorial(n - 1, n * resultado) 

# Função principal, responsável por receber o número e chamar a função fatorial
def main(): 
 n = int(input("Digite um número inteiro: "))
 resultado = fatorial(n)
 print(20* " #") 
 print("Fatorial: ", resultado)
 print(20* " #") 

main()