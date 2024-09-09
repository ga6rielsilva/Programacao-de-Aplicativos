# Função para representar um contato
class Contato:
    def __init__(self, nome, endereco, email):
        self.nome = nome
        self.endereco = endereco
        self.email = email 

# Função para gerenciar a lista de contatos
class Agenda:
    def __init__(self): 
        self.contatos = []

    def adicionar_contato(self, contato):
        self.contatos.append(contato) 

    def remover_contato(self, contato):
        self.contatos.remove(contato)
    def listar_contatos(self):
        for contato in self.contatos: 
            print("Nome:", contato.nome)
            print("Endereço:", contato.endereco) 
            print("E-mail:", contato.email) 

agenda = Agenda()
contato1 = Contato("João", "Rua A, 123", "joao@example.com") 
contato2 = Contato("Maria", "Rua B, 456", "maria@example.com") 

# Adiciona o contato1 e contato2 na lista de contatos
agenda.adicionar_contato(contato1)
agenda.adicionar_contato(contato2)
# Lista os contatos antes de remover o contato1
agenda.listar_contatos()
agenda.remover_contato(contato1)
agenda.listar_contatos()