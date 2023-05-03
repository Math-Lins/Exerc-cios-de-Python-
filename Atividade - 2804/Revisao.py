continuar = "s"
r = []
while continuar == 's':
    a = float(input("Digite a primeira nota: "))
    b = float(input("Digite a segunda nota: "))
    media = (a + b) / 2
    print(media)
    r.append(media)
    if media >=7:
        print("Aprovado", media)
    elif media >= 4 and media <7:
        print("Recuperação", media)
    else:
        print("Reprovado", media)

    continuar = input("Deseja continuar?: ")

