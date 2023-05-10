
"""def nome(n):
    for x in range(n+1):
        for y in range(x):
            print(x, end=" ")
        print()
n = int(input("Digite um número: "))
nome(n)"""

def nome(n):
    for x in range(1,n+1):
        print(str(x)*x)
nome(5)