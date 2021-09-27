n = int(input())
roupas = sorted(input().split())
roupaIgual = 0
for cont in range(len(roupas)-1):
    if roupas[cont] == roupas[cont+1]:
        roupaIgual += 1
print(roupaIgual)