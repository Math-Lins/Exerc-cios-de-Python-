def piramide(n):
    for x in range(1 ,n+1):
        for y in range(1 ,x+1):
            print(y, end=" ")
        print()

n = int(input("Digite um número: "))
piramide(n)