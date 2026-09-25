class Financiamento:
    def __init__(self, veiculo, valor, entrada, num_parcelas):   # init - 10
        self.set_veiculo(veiculo)                                # validação - 10
        self.set_valor(valor)                                    # get/set - 10
        self.set_entrada(entrada)                                # a vista - 10
        self.set_num_parcelas(num_parcelas)                      # parcela - 10
                                                                 # str - 10 
    def get_veiculo(self):                  # print(x.get_veiculo())
        return self.__veiculo
    def set_veiculo(self, veiculo):         # x.set_veiculo("Gol")
        if veiculo == "": raise ValueError("Veículo deve ser informado")
        self.__veiculo = veiculo

    @property         # equivalante ao get      print(x.veiculo)
    def veiculo(self):
        return self.__veiculo
    @veiculo.setter   # equivalente ao set      x.veiculo = "Gol"
    def veiculo(self, veiculo):
        if veiculo == "": raise ValueError("Veículo deve ser informado")
        self.__veiculo = veiculo

    def get_valor(self):
        return self.__valor
    def set_valor(self, valor):
        if valor < 0: raise ValueError("Valor deve ser positivo")
        self.__valor = valor

    def get_entrada(self):
        return self.__entrada
    def set_entrada(self, entrada):
        if entrada < 0: raise ValueError("Entrada deve ser positiva")
        self.__entrada = entrada

    def get_num_parcelas(self):
        return self.__num_parcelas
    def set_num_parcelas(self, num_parcelas):
        if num_parcelas < 1 or num_parcelas > 36: raise ValueError("Número de parcelas deve estar entre 1 e 36")
        self.__num_parcelas = num_parcelas

    def valor_a_vista(self):
        return 0.95 * self.__valor

    @property         
    def a_vista(self):
        return 0.95 * self.__valor
    
    def valor_da_parcela(self):
        return (self.__valor - self.__entrada) / self.__num_parcelas

    def __str__(self):
        return f"{self.__veiculo} - {self.__valor:.2f} - {self.__entrada:.2f} - {self.__num_parcelas}"
        
class UI:
    @staticmethod
    def main():   # while - 10
        op = 0
        while op != 2:
            op = UI.menu()
            if op == 1: UI.calculo()

    @staticmethod
    def menu():   # 10
        print("1 - Financiamento, 2 - Fim")
        return int(input("Escolha uma opção: "))

    @staticmethod
    def calculo(): # 20
        veiculo = input("Nome do veículo: ")
        valor = float(input("Valor do veículo: "))
        entrada = float(input("Valor da entrada: "))
        num_parcelas = int(input("Número de parcelas: "))
        x = Financiamento(veiculo, valor, entrada, num_parcelas)
        print(x.valor_a_vista())
        print(f"{x.valor_a_vista():.2f}")
        print(x.a_vista)
        # x.a_vista = 1000 - Erro por não ter o setter
        print(x.valor_da_parcela())
        print(x)

UI.main()