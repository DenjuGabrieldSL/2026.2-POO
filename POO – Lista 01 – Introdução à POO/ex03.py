class ContaBancaria:
    def __init__(self, titular, numero, saldo):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print("Deposito realizado.")

    def sacar(self, valor):
        if valor <= 0:
            print("Valor invalido.")
        elif valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor
            print("Saque realizado.")

    def verificar_saldo(self):
        return self.saldo


titular = input("Nome do titular: ")
numero = int(input("Numero da conta: "))
saldo = float(input("Saldo inicial: "))

conta = ContaBancaria(titular, numero, saldo)

print("Saldo atual: R$", conta.verificar_saldo())

valor = float(input("Valor para depositar: "))
conta.depositar(valor)

print("Saldo atual: R$", conta.verificar_saldo())

valor = float(input("Valor para sacar: "))
conta.sacar(valor)

print("Saldo final: R$", conta.verificar_saldo())