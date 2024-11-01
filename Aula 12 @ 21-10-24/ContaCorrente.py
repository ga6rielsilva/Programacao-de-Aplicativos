from datetime import datetime
import pytz

class ContaCorrente():

    def __init__(self, titular, cpf, agencia, numeroConta):
        self.titular = titular
        self.cpf = cpf
        self.saldo = 0.0
        self.limite = None
        self.agencia = agencia
        self.numeroConta = numeroConta
        self.transacoes = []

    def Consultar(self):
        return "R$ {:,.2f}".format(self.saldo).replace(",", "v").replace(".", ",").replace("v", ".")

    def Depositar(self, valor):
        self.saldo += valor
        valor = "R$ {:,.2f}".format(self.saldo).replace(",", "v").replace(".", ",").replace("v", ".")
        self.transacoes.append(f"DEP: {valor}, Saldo: {self.Consultar()}, Data e hora: {ContaCorrente._DateHour()}")
        pass

    def Sacar(self, valor):
        if self.saldo - valor < self.Limite():
            print("Você não tem saldo suficiente para fazer isso!")
            self.Consultar()
        else:
            self.saldo -= valor
            valor = "R$ {:,.2f}".format(self.saldo).replace(",", "v").replace(".", ",").replace("v", ".")
            self.transacoes.append(f"SAQ: {valor}, Saldo: {self.Consultar()}, Data e hora: {ContaCorrente._DateHour()}")

    def Transferir(self, valor, contaDestino):
        if self.saldo - valor < self.Limite():
            print("Você não tem saldo suficiente para fazer isso!")
            self.Consultar()
        else:
            self.saldo -= valor
            contaDestino.saldo += valor
            valor = "R$ {:,.2f}".format(self.saldo).replace(",", "v").replace(".", ",").replace("v", ".")

    def Limite(self):
        self.limite = -10000
        return self.limite

    def HistoricoTransacoes(self, transacoes):
        print("Histórico de transações:")
        for transacao in self.transacoes:
            print("-", transacao)

    @staticmethod
    def _DateHour():
        fusoBr = pytz.timezone('Brazil/East')
        horarioBr = datetime.now(fusoBr).strftime('%d/%m/%Y %H:%M:%S')
        return horarioBr

# programa
print("")
lira = ContaCorrente("Lira", "123.456.789-00", "0001", "123456-7")
lira.Depositar(40000)
print(f"Seu saldo atual é: {lira.Consultar()}")
lira.Sacar(10000)
lira.Sacar(10000)
lira.Sacar(10000)
lira.Sacar(10000)
lira.Sacar(10000)
print("")
lira.HistoricoTransacoes(lira.transacoes)
print("")
print(f"Seu saldo atual é: {lira.Consultar()}")
print("")