notas = []
soma = 0
for x in range(5):
    notas.append(float(input("Digite as notas dos alunos: ")))
for y in range(5):
    soma += notas[y]
media = soma / 5
cont = 0
print("Media da turma é: ",media)
for z in range(5):
    if notas[z] >= media:
        cont+=1
print("A quantidade de alunos acima da média é: ",cont)

