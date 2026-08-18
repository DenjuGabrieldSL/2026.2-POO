# Define a função que calcula o teto (ceil) de um número real x
def MenorInteiro(x):
    # Trunca o valor real mantendo apenas a parte inteira
    inteiro = int(x)
    # Se 'x' for maior que sua parte inteira (possui casas decimais), soma 1 ao inteiro
    if x > inteiro:
        return inteiro + 1
    # Caso já seja um número inteiro exato, apenas o retorna
    return inteiro