a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
c = float(input("Digite o terceiro número: "))

if a > b and a > c:
    print("O",a,"é o maior número")
elif b > a and b > c:
    print("O",b,"é o maior número")
else:
    print("O",c,"é o maior número")