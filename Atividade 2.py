print("Determine o número e receba o mês correspondente.")
N1 = int(input("Determine o número:"))

if N1 >= 1 and N1 <= 12:
    if N1 == 1:
        print("Mês correspondente: Janeiro")
    elif N1 == 2:
        print("Mês correspondente: Fevereiro")
    elif N1 == 3:
        print("Mês correspondente: Março")
    elif N1 == 4:
        print("Mês correspondente: Abril")
    elif N1 == 5:
        print("Mês correspondente: Maio")
    elif N1 == 6:
        print("Mês correspondente: Junho")
    elif N1 == 7:
        print("Mês correspondente: Julho")
    elif N1 == 8:
        print("Mês correspondente: Agosto")
    elif N1 == 9:
        print("Mês correspondente: Setembro")
    elif N1 == 10:
        print("Mês correspondente: Outubro")
    elif N1 == 11:
        print("Mês correspondente: Novembro")
    else:
        print("Mês correspondente: Dezembro")
else:
    print("Não condiz com nenhum mês existente.")
