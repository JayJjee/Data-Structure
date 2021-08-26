def verificaPalindromo(lista):
    resposta = True
    while lista:
        c1 = lista.pop(0)
        print(c1)
        c2 = lista.pop()
        print(c2)
        if c1 != c2:
            resposta = False
    return resposta

D = [2,0,0,2]
print(verificaPalindromo(D))
