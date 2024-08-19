from abc import ABC, abstractmethod

# SRP - Responsabilidade única (Classe para operação)
class OperacaoBancaria(ABC):
    @abstractmethod
    def executar(self):
        pass

# SRP - Responsabilidade única (Classe para impressão de mensagens)
class Notificador:
    @staticmethod
    def notificar(mensagem):
        print(mensagem)

# Interface Segregation & Dependency Inversion (Interface da Conta Bancaria)
class IContaBancaria(ABC):
    @abstractmethod
    def depositar(self, valor):
        pass

    @abstractmethod
    def sacar(self, valor):
        pass

    @abstractmethod
    def transferir(self, destinatario, valor):
        pass

# Implementação da interface da Conta Bancária (Classe que adere a SRP)
class ContaBancaria(IContaBancaria):
    def __init__(self, nome, saldo_inicial=0):
        self.nome = nome
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            Notificador.notificar(f"Depósito de R${valor} realizado na {self.nome}. Novo saldo: R${self.saldo}")
        else:
            Notificador.notificar("Valor de depósito inválido. Operação não realizada.")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            Notificador.notificar(f"Saque de R${valor} realizado na {self.nome}. Novo saldo: R${self.saldo}")
        else:
            Notificador.notificar(f"Saldo insuficiente na {self.nome}. Operação não realizada.")

    def transferir(self, destinatario, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            destinatario.depositar(valor)
            Notificador.notificar(f"Transferência de R${valor} realizada da {self.nome} para a {destinatario.nome}. Novo saldo da {self.nome}: R${self.saldo}")
        else:
            Notificador.notificar(f"Saldo insuficiente na {self.nome} ou valor inválido. Transferência não realizada.")

# Open/Closed Principle - Adicionando novos tipos de operações sem modificar a ContaBancaria
class Deposito(OperacaoBancaria):
    def __init__(self, conta, valor):
        self.conta = conta
        self.valor = valor

    def executar(self):
        self.conta.depositar(self.valor)

class Saque(OperacaoBancaria):
    def __init__(self, conta, valor):
        self.conta = conta
        self.valor = valor

    def executar(self):
        self.conta.sacar(self.valor)

class Transferencia(OperacaoBancaria):
    def __init__(self, conta_origem, conta_destino, valor):
        self.conta_origem = conta_origem
        self.conta_destino = conta_destino
        self.valor = valor

    def executar(self):
        self.conta_origem.transferir(self.conta_destino, self.valor)

# SRP - Separação de lógica de entrada do usuário
def obter_valor_input(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            Notificador.notificar("Por favor, insira um valor numérico válido.")

# Execução do Programa Principal com as operações modularizadas
conta1_saldo_inicial = obter_valor_input("Informe o saldo inicial da Conta 1: R$")
conta2_saldo_inicial = obter_valor_input("Informe o saldo inicial da Conta 2: R$")

conta1 = ContaBancaria("Conta 1", conta1_saldo_inicial)
conta2 = ContaBancaria("Conta 2", conta2_saldo_inicial)

while True:
    print("\nOpções:")
    print("1. Depositar na Conta 1")
    print("2. Sacar da Conta 1")
    print("3. Transferir da Conta 1 para a Conta 2")
    print("4. Depositar na Conta 2")
    print("5. Sacar da Conta 2")
    print("6. Transferir da Conta 2 para a Conta 1")
    print("7. Sair")

    escolha = input("Escolha uma opção (1-7): ")

    if escolha == "1":
        valor_deposito = obter_valor_input("Informe o valor a ser depositado na Conta 1: R$")
        Deposito(conta1, valor_deposito).executar()
    elif escolha == "2":
        valor_saque = obter_valor_input("Informe o valor a ser sacado da Conta 1: R$")
        Saque(conta1, valor_saque).executar()
    elif escolha == "3":
        valor_transferencia = obter_valor_input("Informe o valor a ser transferido da Conta 1 para a Conta 2: R$")
        Transferencia(conta1, conta2, valor_transferencia).executar()
    elif escolha == "4":
        valor_deposito = obter_valor_input("Informe o valor a ser depositado na Conta 2: R$")
        Deposito(conta2, valor_deposito).executar()
    elif escolha == "5":
        valor_saque = obter_valor_input("Informe o valor a ser sacado da Conta 2: R$")
        Saque(conta2, valor_saque).executar()
    elif escolha == "6":
        valor_transferencia = obter_valor_input("Informe o valor a ser transferido da Conta 2 para a Conta 1: R$")
        Transferencia(conta2, conta1, valor_transferencia).executar()
    elif escolha == "7":
        break
    else:
        Notificador.notificar("Opção inválida. Tente novamente.")

print("\nSaldos Finais:")
Notificador.notificar(f"Conta 1: R${conta1.saldo}")
Notificador.notificar(f"Conta 2: R${conta2.saldo}")
