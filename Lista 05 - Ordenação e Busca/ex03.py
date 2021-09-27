n = int(input())
listaNota = []
listaOrdem = []
for cont in range(n):
    nota = float(input())
    listaNota.append(nota)

listaOrdem = sorted(listaNota)
print(f"{listaOrdem[0]}")

if len(listaNota) % 2 != 0:
    posMediana = int((round(len(listaOrdem)/2 + 1)))
    print(f"{listaOrdem[posMediana-1]:.2f}")
else:
    posMediana1 = (len(listaOrdem)/2) - 1 
    posMediana2 = (len(listaOrdem)/2) - 2
    mediana = (posMediana1+posMediana2) / 2 
    print(f"{mediana:.2f}")

print(f"{listaOrdem[len(listaOrdem)-1]:.2f}")