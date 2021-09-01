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
fila = Queue()
entrada1 = input().split()
entrada2 = []
entrada3 = []
qntRealizada = int(input())
atvRestam = math.ceil(len(entrada1)/2) - qntRealizada
cont = 0
cont2 = 0
while cont < len(entrada1):
    fila.enqueue(((entrada1[cont]) + " " + (entrada1[cont+1])))
    cont += 2
fila.printar()

'''for cont in range(len(entrada1)):
    fila.enqueue(entrada1[cont])
fila.printar()'''
'''
Comer 1 Academia 2 Dormir 3 ElaborarQuestoes 4 Banhar 5
0
'''