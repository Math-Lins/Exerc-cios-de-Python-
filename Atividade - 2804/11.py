A =[]
for x in range(10):
    A.append(int(input("Digite os números do vetor: ")))
B = int(input("Digite um número ao acaso: "))
cont = 0
for z in range(10):
    if B == A[z]:
        cont+=1
print(cont)
