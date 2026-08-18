# Define a função para checar se o número é primo
def Primo(n):
    # Números menores ou iguais a 1 não são primos por definição
    if n <= 1:
        return False
    # Verifica possíveis divisores de 2 até a raiz quadrada de n
    for i in range(2, int(n**0.5) + 1):
        # Se for divisível por qualquer número nessa faixa, não é primo
        if n % i == 0:
            return False
    # Se não encontrou nenhum divisor, é primo
    return True