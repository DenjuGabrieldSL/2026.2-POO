print("Resultado:")
# Cria um laço de 1 até 10 para a primeira coluna
for i in range(1, 11):
    # Gera uma lista contendo os pares até 'i' convertidos para string
    pares = [str(p) for p in range(2, i + 1, 2)]
    # Formata a linha colocando o valor 'i' seguido dos pares separados por espaço
    linha = f"{i} " + " ".join(pares) if pares else str(i)
    # Exibe a linha gerada
    print(linha)