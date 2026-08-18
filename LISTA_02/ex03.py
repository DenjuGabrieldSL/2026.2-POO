print("A" > "B")
print("A" > "a")
print("2" > "10")
print(2 > 10)

# print("2" > 10)  # erro: não dá para comparar str com int

print(1 > False)  # True
print(1 > True)   # False
print(2 > True)   # True

x = int(input("Digite um numero: "))

if x % 2:
    print("impar")
else:
    print("par")

print("impar" if x % 2 else "par")

for i in range(1, 11):
    print(i)