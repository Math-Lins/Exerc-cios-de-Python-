a = []
soma = 0
for x in range(5):
    a.append(int(input("Digite os números: ")))
print(a)
for z in range(5):
    if a[z]%2 == 0:
        print(a[z])

for w in range(5):
    soma+=a[w]
media = soma/5
#    if a[w] > media:
#        print()
print(soma)
print(media)