# Lógica para converter Km para Metros
def converter_quilometros_para_metros(quilometros):
    metros = quilometros * 1000
    return metros

# Bloco de exceção para tratar erros de entrada
try:
    # Solicita ao usuário a distância em Km
    quilometros = float(input("Digite a distância em quilômetros: "))
    # Convete Km para Metros
    metros = converter_quilometros_para_metros(quilometros)
    print("metros:", metros)
except ValueError:
    # Informa a mensagem caso um valor inválido seja informado
    print("Entrada inválida!")