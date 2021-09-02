import math
class Queue:
    def __init__(self):
        self.fila = []

    def priori(self):
        self.lista = sorted(self.fila, key=lambda priori: priori[1], reverse=True)
        return self.lista

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
print(ativi_priori)

for cont3 in range(qntRealizada):
    ativi_priori.pop()

for cont4 in range(atvRestam):
    print(f'Atividade: {ativi_priori[cont4]}, Prioridade: #{ativi_priori[cont4]}')
print(ativi_priori)

'''
Comer 1 Academia 2 Dormir 3 ElaborarQuestoes 4 Banhar 5
0
'''