eleitores = int(input("Digite o número de eleitores: "))
votob = int(input("Digite o número de votos brancos: "))
voton = int(input("Digite o número de votos nulos: "))
votov = int(input("Digite o número de votos válidos: "))
pvotob = (votob/eleitores)*100
pvoton = (voton/eleitores)*100
pvotov = (votov/eleitores)*100
print("Total de eleitores =",eleitores)
print("Total de votos brancos =",votob)
print("Total de votos nulos =",voton)
print("Total de votos válidos =",votov)
print(pvotob,"% de votos brancos")
print(pvoton,"% de votos nulos")
print(pvotov,"% de votos válidos")