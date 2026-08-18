# Lê a string fornecida
frase = input("Digite uma frase:\n")
# Imprime a frase original primeiro
print(frase)

# Armazena a string em uma variável que mudará a cada iteração
atual = frase
# Repete o processo pela mesma quantidade de caracteres da frase
for _ in range(len(frase)):
    # Pega do segundo caractere em diante [1:] e concatena o primeiro caractere [0] no final
    atual = atual[1:] + atual[0]
    # Exibe a palavra rotacionada
    print(atual)