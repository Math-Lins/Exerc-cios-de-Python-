def somar(A, B):
    Soma = A + B
    print("A soma é: ", Soma)
def subtrair (A,B):
    Subtrai = A - B
    print("A subtração é: ", Subtrai)
def multiplicar (A,B):
    Multiplica = A * B
    print("A multiplicação é:", Multiplica)
def dividir (A,B):
    Divida = A/B
    print("A divisão é: ", Divida)

while True:
    N1 = float(input("Digite o primeiro número: "))
    N2 = float(input("Digite o segundo número: "))
    x = int(input("Escolha um número dentre o intervalo de 1 entre 5: "))

    if x == 1:
        somar(N1, N2)
    elif x == 2:
        subtrair(N1, N2)
    elif x == 3:
        multiplicar(N1, N2)
    elif x == 4:
        dividir(N1, N2)
    else:
        print("Obrigado por usar a ferramenta! :) ")
        break




