import math

class Queue:
    def __init__(self):
        self.fila = []

    def priori(self):
        self.lista = sorted(self.fila, key=lambda priori: priori[1])
        return self.lista

    def dequeue(self):
        return self.fila.pop()

    def enqueue(self, item):
        self.fila.append(item)

    def isEmpty(self):
        return self.fila == []

    def size(self):
        return len(self.fila)
    
    def printar(self):
        return print(self.fila)

entrada1 = input().split()
qntRealizada = int(input())
atvRestam = math.ceil(len(entrada1)/2) - qntRealizada
entradaDiv = math.ceil(len(entrada1)/2)
atividade = []
prioridade = []
ativi_priori = 0
fila = Queue()

for cont in range(len(entrada1)):
    if cont % 2 != 0:
        prioridade.append(entrada1[cont])
    elif cont % 2 == 0:
        atividade.append(entrada1[cont])

print(f"Tamanho da fila: {atvRestam}")
for cont2 in range(entradaDiv):
    fila.enqueue((atividade[cont2],prioridade[cont2]))
ativi_priori = fila.priori()

for cont3 in range(qntRealizada):
    ativi_priori.pop(0)

for cont4 in ativi_priori:
    print(f'Atividade: {cont4[0]}, Prioridade: #{cont4[1]}')

'''
A 1 B 2 C 3 D 4 E 5 F 1
0
'''