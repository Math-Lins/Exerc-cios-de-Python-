def numeros_unicos(lista):
    nova_lista = []
    for num in lista:
        if num not in nova_lista:
            nova_lista.append(num)
    return nova_lista

lista = [1,2,2,3,4,4,5,3,6,7,6,8]
resultado = numeros_unicos(lista)
print(resultado)

