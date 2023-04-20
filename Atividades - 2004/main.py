"""N1 = float(input("Digite o primeiro número: "))
N2 = float(input("Digite o segundo número: "))

subtracao = N1 - N2
multiplicacao = N1 * N2
divisao = N1 / N2
x = int(input("Escolha um número dentre o intervalo de 1 entre 6: "))

while x == 5:
    N1 = float(input("Digite o primeiro número: "))
    N2 = float(input("Digite o segundo número: "))

    while x != 5:
        if x == 1:
            print("A soma dos dois números é: ", (N1 + N2))


        elif x == 2:
            print("A subtração dos dois números é: ", subtracao)


        elif x == 3:
            print("A multiplicação dos dois números é: ", multiplicacao)


        elif x == 4:
            print("A divisão dos dois números é: ")


        elif x == 6:
            print("Obrigado por usar a ferramenta :)")
            break
"""
resp =0
while resp !=6:
    N1 = float(input("Digite o primeiro número: "))
    N2 = float(input("Digite o segundo número: "))

    while True:
        resp = int(input("Digite 1 para somar \n"
                         "Digite 2 para sub \n"
                         "Digite 3 para mult \n"
                         "Digite 4 para dividir\n"
                         "Digite 5 para solicitar\n"
                         "Digite 6 para sair\n"))

        match resp:
            case 1:
                print(N1 + N2)
            case 2:
                print(N1 - N2)
            case 3:
                print(N1 * N2)
            case 4:
                print(N1/N2)
            case 5:
                break
            case 6:
                break
