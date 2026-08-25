x = int(input("informe um número:"))
y = int(input("informe um número:"))

# MMC
def MMC(x, y):
    m = x
    while m % x != 0 or m % y != 0:
        m = m + 1
    return m

# MDC
def MDC(x, y):
    d = x
    while x % d != 0 or y % d != 0:
        d = d - 1
    return d

def MDC2(x, y):
    if x % y == 0: return y
    MDC2(y, x % y)

    return x * y / MDC(x, y)

# MMC * MDC = x * y -> MMC = x * y / MDC

print("MMC =", MDC(x, y))
print("MDC =", MDC(x, y))
print("Prod= ", x * y)
print("MMC * MDC = ", MDC(x, y) * MDC(x, y))