listaPremios = input().split()
numSort = int(input())
tamLista = len(listaPremios)-1

def somatoria(n):
    for cont in range(n, 0, -1):
        if cont != n and listaPremios[cont]+listaPremios[n] == numSort:
            return 'E possivel ganhar'
    if n == 0:
        return 'Impossivel ganhar.'
    else:
        return somatoria(n-1)

print(somatoria(tamLista))