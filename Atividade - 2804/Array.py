A = []
B = []
C = []
N = int(input("Digite um valor: "))
for x in range(N):
    A.append(int(input("Digite os números da lista A: ")))
    B.append(int(input("Digite os números da lista B: ")))
    soma = A[x] + B[x]
    C.append(soma)

print(A)
print(B)
print(C)