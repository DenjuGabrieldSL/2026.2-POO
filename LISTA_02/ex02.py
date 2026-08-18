x = [4, 5, 6]
#y = x    # x e y sao a mesma lista
y = x [:] # x e y sao listas diferentes
y.append(7)
print(x, id(x))
print(y, id(y))

a = 5
b = a
b = 6
print(a, id(a))
print(b, id(b))

# nas linguagem C++, C#, Java
# 'C' - char
# "C" - string

# no python
# 'C' - string
# "C" - string

s = "tecnologia"
print (s[0:6])

x = 5
y = x == 5
print(y)
print(type(y))

x = 1/4
y = 1.0/4
y = y = 1/4.0

"""
print(5 * "TADS")
print(5 + "5")  # erro
"""