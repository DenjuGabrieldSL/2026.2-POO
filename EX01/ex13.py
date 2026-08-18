# Define a função para limpar espaços sobressalentes
def RemoverEspacos(texto):
    # 'texto.split()' divide o texto ignorando múltiplos espaços consecutivos;
    # '" ".join(...)' reúne as palavras utilizando exatamente 1 espaço entre elas.
    return " ".join(texto.split())