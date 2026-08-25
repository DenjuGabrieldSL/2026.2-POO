x = int(input("informe um número: "))
y = int(input("informe um número: "))

d = x
while x % d != 0 or y % d != 0:
    d = d - 1

print("MDC =", d)
