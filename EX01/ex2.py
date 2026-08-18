# Lista com os nomes de todos os meses do ano em ordem
meses = [
    "janeiro", "fevereiro", "março", "abril", "maio", "junho",
    "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
]
# Lista com a escrita ordinal dos quatro trimestres
trimestres = ["primeiro", "segundo", "terceiro", "quarto"]

# Solicita a entrada e converte para valor inteiro
num_mes = int(input("Informe o número do mês\n"))

# Valida se o número digitado está na faixa válida de meses (1 a 12)
if 1 <= num_mes <= 12:
    # Obtém o nome do mês ajustando o índice (listas começam em 0)
    nome_mes = meses[num_mes - 1]
    # Usa divisão inteira por 3 para mapear o mês no seu respectivo trimestre
    trimestre = trimestres[(num_mes - 1) // 3]
    # Imprime a frase formatada com as informações obtidas
    print(f"O mês de {nome_mes} é do {trimestre} trimestre do ano")
else:
    # Exibe mensagem de erro se o valor informado for menor que 1 ou maior que 12
    print("Mês inválido!")