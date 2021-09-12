from itertools import combinations

listaPremios = input().split()
listaPremios2 = [int(i) for i in listaPremios]
numSort = int(input())
bPossivel = False

def somatoria(r):
    global bPossivel
    if r > len(listaPremios2)+1:
        return
    somas = []
    somas += list(combinations(listaPremios2, r))
    for lista in somas:
        if sum(lista) == numSort:
            bPossivel = True
            return
    somatoria(r+1)

if len(listaPremios2) == 1:
    if numSort == listaPremios2[0]:
        bPossivel = True
else:
    somatoria(2)

if bPossivel == True:
    print("E possivel ganhar.")
else:
    print("Impossivel ganhar.")