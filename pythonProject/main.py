class ContaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def depositar(self, valor, conta_nome):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor} realizado na {conta_nome}. Novo saldo: R${self.saldo}")
        else:
            print("Valor de depósito inválido. Operação não realizada.")

    def sacar(self, valor, conta_nome):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado na {conta_nome}. Novo saldo: R${self.saldo}")
        else:
            print(f"Saldo insuficiente na {conta_nome}. Operação não realizada.")

    def transferir(self, destinatario, valor, conta_nome_origem, conta_nome_destino):
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                destinatario.depositar(valor, conta_nome_destino)
                print(f"Transferência de R${valor} realizada da {conta_nome_origem} para a {conta_nome_destino}. Novo saldo da {conta_nome_origem}: R${self.saldo}")
            else:
                print(f"Saldo insuficiente na {conta_nome_origem}. Transferência não realizada.")
        else:
            print("Valor inválido para transferência. Transferência não realizada.")

def obter_valor_input(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("Por favor, insira um valor numérico válido.")

conta1_saldo_inicial = obter_valor_input("Informe o saldo inicial da conta 1: R$")
conta2_saldo_inicial = obter_valor_input("Informe o saldo inicial da conta 2: R$")

conta1 = ContaBancaria(conta1_saldo_inicial)
conta2 = ContaBancaria(conta2_saldo_inicial)

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
        conta1.depositar(valor_deposito, "Conta 1")
    elif escolha == "2":
        valor_saque = obter_valor_input("Informe o valor a ser sacado da Conta 1: R$")
        conta1.sacar(valor_saque, "Conta 1")
    elif escolha == "3":
        valor_transferencia = obter_valor_input("Informe o valor a ser transferido da Conta 1 para a Conta 2: R$")
        conta1.transferir(conta2, valor_transferencia, "Conta 1", "Conta 2")
    elif escolha == "4":
        valor_deposito = obter_valor_input("Informe o valor a ser depositado na Conta 2: R$")
        conta2.depositar(valor_deposito, "Conta 2")
    elif escolha == "5":
        valor_saque = obter_valor_input("Informe o valor a ser sacado da Conta 2: R$")
        conta2.sacar(valor_saque, "Conta 2")
    elif escolha == "6":
        valor_transferencia = obter_valor_input("Informe o valor a ser transferido da Conta 2 para a Conta 1: R$")
        conta2.transferir(conta1, valor_transferencia, "Conta 2", "Conta 1")
    elif escolha == "7":
        break
    else:
        print("Opção inválida. Tente novamente.")

print("\nSaldos Finais:")
print(f"Conta 1: R${conta1.saldo}")
print(f"Conta 2: R${conta2.saldo}")
