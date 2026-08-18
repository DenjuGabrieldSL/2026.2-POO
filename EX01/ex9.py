# Lê a frase fornecida
frase = input("Digite uma frase:\n")
# Separa a frase pelas palavras
palavras = frase.split()

# Itera sobre cada palavra obtida
for palavra in palavras:
    # Utiliza fatiamento com passo -1 [::-1] para inverter a palavra e a imprime
    print(palavra[::-1])