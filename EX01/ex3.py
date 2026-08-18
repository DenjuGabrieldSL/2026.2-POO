print("Digite quatro valores inteiros")
# Lê 4 valores inteiros informados pelo usuário e os armazena em uma lista
valores = [int(input()) for _ in range(4)]

# Converte a lista em 'set' (conjunto), que remove duplicatas, e compara a quantidade
if len(set(valores)) != 4:
    # Exibe erro caso o tamanho do conjunto seja menor que 4 (há números repetidos)
    print("Erro: Os valores digitados não são todos diferentes!")
else:
    # Ordena os valores em ordem crescente
    valores_ordenados = sorted(valores)
    # O maior número fica no último índice (3)
    maior = valores_ordenados[3]
    # O menor número fica no primeiro índice (0)
    menor = valores_ordenados[0]
    # Soma o segundo menor (índice 1) com o segundo maior (índice 2)
    soma_intermediarios = valores_ordenados[1] + valores_ordenados[2]
    
    # Exibe os resultados calculados
    print(f"Maior valor = {maior}")
    print(f"Menor valor = {menor}")
    print(f"A soma do segundo maior valor com o segundo menor = {soma_intermediarios}")