def primos():
    n = int(input("Digite um número: "))
    if n > 1:
        for x in range(2,n):
            if n%x ==0:
                print(n,"Não é primo")
                break
        else:
            print(n,"É número primo")
    elif n == 0:
        print("Este número é 0")
    elif n == 1:
        print("1 não é primo")
    else:
        print(n,"Número negativo")




