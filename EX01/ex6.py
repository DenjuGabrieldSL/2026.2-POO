# Cria uma lista onde números ímpares ficam positivos e pares ficam negativos (1 a 10)
resultado = [i if i % 2 != 0 else -i for i in range(1, 11)]
# Junta todos os elementos convertidos para texto por um espaço e exibe
print("Resultado:", " ".join(map(str, resultado)))