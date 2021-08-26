def decrescente(*numeros):
    N = tuple(sorted(numeros, reverse = True))
    return N
print(decrescente(2, 3, 1))