class ContaBancaria:
    def __init__(self,titular):
        self.__titular = titular
        self.__saldo = 0

    def depositar(self,valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("o valor deve ser positivo")
    def sacar(self,valor):
        if valor <= 0:
            print("o valor sacado deve ser positivo")
        elif valor > self.__saldo:
            print("saldo insuficiente")
        else:
            self.__saldo -= valor
    
    def exibirSaldo(self):
        print(f"saldo do cliente {self.__titular} é R$ {self.__saldo:.2f}")


nomeDoTitular = input("digite o Nome do Titular da conta:  ")

depositarDinheiro = int(input("valor a ser depositado  "))
sacarDinheiro = int(input("valor a ser sacado  "))
conta = ContaBancaria(nomeDoTitular)
conta.depositar(depositarDinheiro)
conta.sacar(sacarDinheiro)
conta.exibirSaldo()



