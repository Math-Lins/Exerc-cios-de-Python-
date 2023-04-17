print("Cálculo da Média dos alunos nas duas primeiras avaliações.")
Aluno = input("Digite o nome do aluno: ")

resp = "s"
while resp=="s":
    N1 = float(input("Digite a nota da primeira avaliação: "))
    while N1 < 0 or N1 > 10:
        print("Nota inválida, digite novamente com um número válido entre 0 e 10: ")
        N1 = float(input("Digite a nota da primeira avaliação: "))

    N2 = float(input("Digite a nota da segunda avaliação: "))
    while N2 < 0 or N2 > 10:
        print("Nota inválida, digite novamente com um número válido entre 0 e 10: ")
        N2 = float(input("Digite a nota da segunda avaliação: "))

    Media = (N1 + N2)/2
    print("Média do aluno", Aluno,"é : ",Media)
    resp = input("Deseja continuar? ")