# Lê a frase fornecida
frase = input("Digite uma frase:\n")
# Quebra a frase em uma lista contendo cada palavra individualmente
palavras = frase.split()

# Percorre os índices da lista de palavras
for i in range(len(palavras)):
    # Imprime as palavras restantes do índice 'i' em diante juntas por espaço
    print(" ".join(palavras[i:]))