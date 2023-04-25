A = []
mult = 0
M = []
for y in range(10):
    A.append(int(input("Digite os 10 números da lista: ")))
x = int(input("Digite um valor para x: "))
for z in range(10):
    mult = x*A[z]
    M.append(mult)
print(A)
print(x)
print(M)

