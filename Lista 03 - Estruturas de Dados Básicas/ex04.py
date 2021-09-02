import math
class Queue:
    def __init__(self):
        self.fila = []

    def dequeue(self):
        return self.fila.pop()

    def enqueue(self, item):
        self.fila.insert(0,item)

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
ativi_priori = []
fila = Queue()

for cont in range(len(entrada1)):
    if cont % 2 != 0:
        prioridade.append(entrada1[cont])
    elif cont % 2 == 0:
        atividade.append(entrada1[cont])

print(f"Tamanho da fila: {atvRestam}")
for cont2 in range(entradaDiv):
    ativi_priori.append((atividade[cont2],prioridade[cont2]))

fila.enqueue(sorted(ativi_priori, key=lambda prioridade: prioridade[1]))
fila.printar()

'''
Comer 1 Academia 2 Dormir 3 ElaborarQuestoes 4 Banhar 5
0
'''