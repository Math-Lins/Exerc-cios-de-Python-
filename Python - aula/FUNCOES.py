"""def somar(A, B):
    return A + B"""

def subtrair (A,B):
    return A - B

def multiplicar (A,B):
    return A*B

def dividir (A,B):
    return A/B

def estoque(produto, quantidade,valor):
    return produto, quantidade*valor

def somar(*numeros):
    total =0
    for x in numeros:
        total +=x
    return total

def texto(t):
    textoi=""
    cont = 0
    for x in range(len(t)-1,-1,-1):
        textoi+= t[x]
        if t[x] != " ":
            cont+=1
    return t, cont, textoi

def test_primo(n):
    if n == 1:
        return n, "Não é primo"
    elif n == 2:
        return n, "É primo"
    else:
        for x in range(2,n):
            if n%x==0:
                return n,"Não é primo"
        return n,"É primo"






















