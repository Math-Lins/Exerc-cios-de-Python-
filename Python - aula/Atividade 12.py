class ContaBancaria:
    def __init__(self, numero_conta, nome_cliente, tipo_conta):
        self.numero_conta = numero_conta
        self.saldo = 0
        self.status_conta = False
        self.nome_cliente = nome_cliente
        self.tipo_conta = tipo_conta
        self.limite = 0

    def ativar_conta(self):
        if self.saldo == 0:
            self.status_conta = True
            print("A conta está ativa.")
        else:
            print("Não é possível ativar conta com saldo diferente de zero.")

    def desativar_conta(self):
        if self.saldo ==0:
            self.status_conta = True
            print("Conta desativada")
        else:
            print("Sua conta está ativa.")

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print("Depósito realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")

    def verificar_saldo(self):
        if self.ativar_conta == False:
            print("Conta não está ativa")
        else:
             print(f"Saldo disponível: R${self.saldo: }")

    def sacar(self, valor):
        if self.status_conta == True:
            if valor > 0 and valor <= self.saldo:
                self.saldo -= valor
                print("Saque realizado com sucesso.")
            else:
                print("Saldo insuficiente ou valor inválido para saque.")
        else:
            print("Não é possível sacar de uma conta que não foi ativa.")



    def ativar_limite (self, valor_limite):
        if self.status_conta == True:
            if self.limite == 0:
               self.limite = valor_limite
            print(f"Limite atual de R${self.limite}.")


    def desativar_limite (self, valor_limite):
        if self.limite > 0:
           self.limite = valor_limite
           print(f"Limite atual de R${self.limite}.")




conta = ContaBancaria("401758-0", "Matheus", "Corrente")
conta.ativar_conta()
conta.verificar_saldo()
conta.ativar_limite(2000.00)
conta.depositar(200.0)

conta.verificar_saldo()

conta.sacar(100.0)
conta.verificar_saldo()

conta.sacar(50.0)
conta.verificar_saldo()
conta.desativar_conta()
conta.sacar(50.0)
conta.verificar_saldo()
conta.desativar_conta()
