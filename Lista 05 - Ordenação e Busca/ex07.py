n = int(input())
listaNomes = []
tam = 0

def count_chars(txt):
	result = 0
	for char in txt:
		result += 1

for cont in range(n):
    nomee = input()
    nome = list(nomee)
    listaNomes.append(nome)      
    listaOrdenada = sorted(listaNomes, key=len)

''''for cont2 in range(len(listaOrdenada)-1):
    if len(listaOrdenada[cont2]) == len(listaOrdenada[cont2+1]):
        listaOrdenada.remove(listaOrdenada[cont2])
        listaOrdenada.remove(listaOrdenada[cont2+1])'''
print(listaOrdenada)
