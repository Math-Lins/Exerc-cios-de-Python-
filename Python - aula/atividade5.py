from FUNCOES import *
variavel = estoque("Celular", 50, 2000)

print("O estoque de ",variavel[0], ", custa: ", variavel[1])

nome, valor = estoque("arroz", 5, 80)
print(f"O produto {nome} custa {valor}")

x = somar(5,10,20,30)
print(x)