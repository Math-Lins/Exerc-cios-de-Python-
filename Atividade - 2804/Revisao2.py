continuar = 's'
while continuar == 's':
    a = float(input("Digite um número: "))
    if a == 0:
        print("Opa, igual a 0")
    elif a > 0:
        print("Teu número é inteiro positivo")
    else:
        print("Teu número é inteiro negativo")
    continuar = input("Deseja continuar? ")
print("Obrigado por utilizar os serviços da Matheus Enterprises!")