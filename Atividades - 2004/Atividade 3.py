alunos = []
n=int(input("Digite o número de alunos na sala: "))
for x in range(n):
    alunos.append(input("Digite o nome dos alunos: "))
for y in range (n):
    print(y, alunos[y])