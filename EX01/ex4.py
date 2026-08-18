# Função auxiliar para checar se um ano é bissexto
def eh_bissexto(ano):
    # Retorna True se o ano for divisível por 4 e não por 100, ou se for divisível por 400
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

# Solicita a leitura da data em texto
data_str = input("Digite uma data no formato dd/mm/aaaa\n")

try:
    # Divide a string nas barras e converte dia, mês e ano para inteiros
    dia, mes, ano = map(int, data_str.split('/'))
    # Define a variável indicadora como válida inicialmente
    valida = True
    
    # Verifica se o ano está dentro dos limites [1900, 2100] e mês dentro de [1, 12]
    if not (1900 <= ano <= 2100) or not (1 <= mes <= 12):
        valida = False
    else:
        # Define a quantidade máxima de dias de cada mês (fevereiro ajusta com eh_bissexto)
        dias_no_mes = [31, 29 if eh_bissexto(ano) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        # Valida se o dia informado cabe no mês especificado
        if not (1 <= dia <= dias_no_mes[mes - 1]):
            valida = False

    # Exibe resultado final dependendo do valor da variável valida
    if valida:
        print("A data informada é válida")
    else:
        print("A data informada não é válida")
except ValueError:
    # Caso ocorra falha ao separar ou converter os inteiros (formato ruim)
    print("A data informada não é válida")