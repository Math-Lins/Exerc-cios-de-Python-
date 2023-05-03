continuar = 's'
while continuar == 's':
    a = int(input("Digite um número: "))
    if a%2 == 0:
        if a > 0:
            print("Par e positivo")
        else:
            print("Par e negativo")
    else:
        if a > 0:
            print("Ímpar e positivo")
        else:
            print("Ímpar e negativo")
    continuar = input("Deseja continuar?: ")
print("Obrigado por utilizar os serviços")