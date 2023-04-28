Nome = []
Senhas = []

for x in range(5):
    Nome.append(input("Digite os nomes da lista: "))
    Senhas.append(int(input("Digite as senhas dos usuários: ")))
cont = 0
q = input("Digite o login: ")
w = int(input("Digite a senha: "))
for z in range(5):

    if q == Nome[z] and w == Senhas[z]:
        print("Login efetuado com sucesso!")
        break
    else:
        cont += 1
if cont == 5:
    print("Acesso negado!")

