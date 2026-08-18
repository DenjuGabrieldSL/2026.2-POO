print ("olá")
print()
x = print() # x é o print
print(x)    # x é o retorno do print = None
print(type(x))
x("tudo bem?")

def quadrado (n):
    return n ** 2

print(quadrado(4))

x = quadrado
print(x(4))

x = lambda n : n ** 2
print(x(4))

x = lambda a, b : a + b
print (x(4, 6))



