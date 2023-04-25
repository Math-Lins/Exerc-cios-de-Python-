alunos = []
n=int(input("Digite o número de alunos na sala: "))
for x in range(n):
    alunos.append(input("Digite o nome dos alunos: "))
"""for y in range (n):
    print(y, alunos[y])"""
z = input("Digite um nome da lista: ")
cont = 0
for w in range(n):
    if z == alunos[w]:
        print(w, alunos[w])
    else:
        cont+=1
if cont == n:
    print("Não encontrado")





