print("Digite três valores:")
# Lê os 3 valores em ponto flutuante
a = float(input())
b = float(input())
c = float(input())

# Troca 'a' e 'b' de lugar se 'a' for maior, garantindo a <= b
if a > b:
    a, b = b, a
# Troca 'a' e 'c' de lugar se 'a' for maior, garantindo que 'a' receba o menor de todos
if a > c:
    a, c = c, a
# Troca 'b' e 'c' de lugar se 'b' for maior, organizando 'b' e 'c'
if b > c:
    b, c = c, b

# Imprime os 3 valores já trocados em ordem crescente (:g remove zeros decimais se forem inteiros)
print(f"{a:g}, {b:g}, {c:g}")