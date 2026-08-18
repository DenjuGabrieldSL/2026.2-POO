# Inicializa a variável que vai acumular a soma dos números pares
pares = 0
# Inicializa a variável que vai acumular a soma dos números ímpares
impares = 0

print("Digite quatro valores inteiros")
# Cria um laço que irá rodar exatamente 4 vezes
for _ in range(4):
    # Lê a entrada do usuário e converte para número inteiro
    num = int(input())
    # Verifica se o resto da divisão por 2 é igual a 0 (se o número é par)
    if num % 2 == 0:
        # Adiciona o número ao acumulador de pares
        pares += num
    else:
        # Caso contrário, adiciona o número ao acumulador de ímpares
        impares += num

# Exibe a soma final dos pares
print(f"Soma dos pares = {pares}")
# Exibe a soma final dos ímpares
print(f"Soma dos ímpares = {impares}")