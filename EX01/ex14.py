# Importa o módulo 'math' para acessar a função de Máximo Divisor Comum (gcd)
import math

# Define a função que calcula o Mínimo Múltiplo Comum entre x e y
def MMC(x, y):
    # Usa a relação: MMC(x, y) = (|x * y|) / MDC(x, y)
    return (x * y) // math.gcd(x, y)