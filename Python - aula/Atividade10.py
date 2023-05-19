palavra_secreta = 'Bumerangue'
digitado = []
chances = 3
print("_________________________________________")
print("---------------Jogo da forca-------------")
print("Tente adivinhar qual a palavra escolhida!")
print("_________________________________________")
while True:
    letra = str(input("Digite a primeira letra: "))
    if len(letra)>1:
        print('Não pode mais que um caractere!!!')
        continue
    digitado.append(letra)
    palavra_temporaria = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in digitado:
            palavra_temporaria += letra_secreta
        else:
            palavra_temporaria += '*'
    if palavra_temporaria == palavra_secreta:
        print("You are the champion, my friend!")
        break
    else:
        print(f'A palavra é assim: {palavra_temporaria}')
    if letra not in palavra_secreta:
        chances -= 1
    if chances <=0:
        print("Perdeu meu parça!")
        break
    print(f'Você tem {chances} tentativas.')
    print()